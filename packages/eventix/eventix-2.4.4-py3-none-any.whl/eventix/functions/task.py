import datetime
import logging
from typing import List, Tuple

from pydantic_db_backend_common.exceptions import RevisionConflict
from pydantic_db_backend_common.utils import utcnow

from eventix.exceptions import NoTaskFoundForUniqueKey, WrongTaskStatus
from eventix.functions.features import backend_features
from eventix.pydantic.pagination import PaginationParametersModel
from eventix.pydantic.task import TaskModel, task_model_status
from pydantic_db_backend.backend import Backend

# post
# already exists
# still scheduled -> update
# not scheduled --> post new.
# scheduled -> update
#
#   on update:
#       get task
#       scheck scheduled, if not post
#       update task
#
#       if worker grabs , version should conflict
#       on conflict : try again

log = logging.getLogger(__name__)


def task_post(task: TaskModel) -> TaskModel:
    is_unique = task.unique_key is not None
    client = Backend.client()

    if not is_unique:
        # not unique , just try to save. If exists, raise error
        # noinspection PyTypeChecker
        return client.post_instance(task)

    # has unique_key

    while True:

        # noinspection PyTypeChecker
        existing_tasks: List[TaskModel] = client.get_instances(TaskModel, 0, 10, {"unique_key": task.unique_key})
        next_scheduled_task = next(filter(lambda t: t.status in ("scheduled", "retry"), existing_tasks), None)

        if next_scheduled_task is None:
            # no existing ones that are only scheduled, we have to post
            # noinspection PyTypeChecker
            return client.post_instance(task)

        #   update:
        #       get task
        #       scheck scheduled, if not post
        #       update task
        #
        #       if worker grabs , version should conflict
        #       on conflict: try again

        next_scheduled_task.unique_update_from(task)
        try:
            updated_task = client.put_instance(next_scheduled_task)
            # noinspection PyTypeChecker
            log.debug(f"updated task {updated_task.uid}")
            # noinspection PyTypeChecker
            return updated_task  # update worked
        except RevisionConflict:
            continue  # try again.


def task_clean_expired_workers():
    client = Backend.client()
    params = dict(
        model=TaskModel,
        skip=0,
        limit=1,
        query_filter=dict(
            worker_expires={
                "$and": [
                    {"$ne": None},
                    {"$lt": utcnow()},
                ]
            }  # no worker assigned
        ),
        sort=[
            {"priority": "asc"},
            {"eta": "asc"}
        ]
    )

    while True:
        # noinspection PyTypeChecker
        existing_task: TaskModel | None = next(iter(client.get_instances(**params)), None)

        # repeat until we were able to take something or nothing is left.
        if existing_task is None:
            break

        existing_task.status = "scheduled"
        existing_task.worker_id = None
        existing_task.worker_expires = None

        try:
            client.put_instance(existing_task)
            log.info(f"Released task {existing_task.uid}")
            # noinspection PyTypeChecker
        except RevisionConflict:
            continue


def task_clean_expired_tasks():
    client = Backend.client()
    params = dict(
        model=TaskModel,
        skip=0,
        limit=100,
        query_filter=dict(
            expires={
                "$and": [
                    {"$ne": None},
                    {"$lt": utcnow()},
                ]
            }  # task expired
        ),
        # sort=[
        #     {"priority": "asc"},
        #     {"eta": "asc"}
        # ]
    )

    while True:
        # noinspection PyTypeChecker
        existing_uids = client.get_uids(**params)

        # repeat until we were able to take something or nothing is left.
        if len(existing_uids) == 0:
            break

        for uid in existing_uids:
            client.delete_uid(TaskModel, uid)
            log.info(f"Removed expired task {uid}")


def task_next_scheduled(worker_id: str, namespace: str, expires: int = 300) -> TaskModel | None:
    log.debug(f"[{worker_id}] Worker getting next scheduled task...")
    client = Backend.client()

    # looking up possible tasks in right order
    # take first one
    # try to set worker_id and expiration

    eta = utcnow().isoformat()  # eta has to be now or in the past

    query_filter = dict(
        namespace=namespace,  # namespace has to match
        worker_id=None,  # no worker assigned
        status={"$in": ["scheduled", "retry"]},
        eta={"$lte": eta}
    )
    sort = [
        {"priority": "asc"},
        {"eta": "asc"}
    ]

    while True:  # repeat until we were able to take something or nothing is left.

        # noinspection PyTypeChecker
        existing_task: TaskModel | None = next(iter(client.get_instances(
            TaskModel,
            0,
            1,
            query_filter=query_filter,
            sort=sort
        )), None)

        if existing_task is None:
            return None  # no task left

        existing_task.status = "processing"
        existing_task.worker_id = worker_id
        existing_task.worker_expires = utcnow() + datetime.timedelta(seconds=expires)
        log.debug(f"task_next_scheduled: existing task revision: {existing_task.revision}")
        try:
            # noinspection PyTypeChecker
            t: TaskModel = client.put_instance(existing_task)
            return t
        except RevisionConflict:
            continue


def tasks_by_status(
    status: task_model_status | None = None,
    namespace: str | None = None,
    pagination: PaginationParametersModel | None = None,
    max_results: bool | None = True
) -> Tuple[List[TaskModel], int]:
    client = Backend.client()

    query_filter = {}
    if status is not None:
        query_filter["status"] = {"$eq": status}
    if namespace is not None:
        query_filter["namespace"] = {"$eq": namespace}
    params = {
        "query_filter": query_filter,
        **pagination.model_dump(exclude_none=True),
    }

    # noinspection PyTypeChecker
    tasks = client.get_instances(TaskModel, **params, max_results=max_results)
    if max_results is True:
        tasks, max_results = tasks
    else:
        max_results = 0

    tasks: List[TaskModel]
    return tasks, max_results


@backend_features(features=["find_extend_pipeline"])
def tasks_by_task(
    task: str = None,
    namespace: str | None = None,
    pagination: PaginationParametersModel | None = None
) -> Tuple[List[TaskModel], int]:
    client = Backend.client()

    query_filter = {"task": {"$eq": task}}
    if namespace is not None:
        query_filter["namespace"] = {"$eq": namespace}

    ep = [
        {
            "$addFields": {
                "status_id": {
                    "$indexOfArray": [
                        ['scheduled', "processing", "retry", "error", "done"],
                        "$status"
                    ]
                }
            }
        }
    ]

    pagination_params = pagination.model_dump(exclude_none=True)

    params = {
                 "query_filter": query_filter,
                 "extend_pipeline": ep,
                 "sort": [{"status_id": "asc"}, {"scheduled": "desc"}]
             } | pagination_params

    # noinspection PyTypeChecker
    tasks, max_results = client.get_instances(TaskModel, **params, max_results=True)
    return tasks, max_results


def task_by_unique_key(unique_key: str) -> TaskModel:
    # noinspection PyTypeChecker
    existing_tasks: List[TaskModel] = Backend.client().get_instances(TaskModel, 0, 10, {"unique_key": unique_key})
    found = next(filter(lambda t: t.status in ("scheduled", "retry"), existing_tasks), None)
    if found is None:
        raise NoTaskFoundForUniqueKey(unique_key=unique_key)

    return found


def task_reschedule(uid: str, eta: datetime.datetime | None = None) -> TaskModel:
    # noinspection PyTypeChecker
    t: TaskModel = Backend.client().get_instance(TaskModel, uid)

    if t.status not in ["error", "retry"]:
        raise WrongTaskStatus(uid, t.status)

    if eta is None:
        eta = utcnow()

    t.status = "scheduled"
    t.eta = eta
    t.worker_id = None
    Backend.client().put_instance(t)
    return t


def tasks_dump(
    # task: str = None,
    # namespace: str | None = None,
    pagination: PaginationParametersModel | None = None
) -> Tuple[List[TaskModel], int]:
    client = Backend.client()

    # query_filter = {"task": {"$eq": task}}
    # if namespace is not None:
    #     query_filter["namespace"] = {"$eq": namespace}

    pagination_params = {} if pagination is None else pagination.model_dump(exclude_none=True)

    params = {
                 "sort": [{"_id": "asc"}]
             } | pagination_params

    # noinspection PyTypeChecker
    tasks = client.get_instances(TaskModel, **params, max_results=False)
    return tasks
