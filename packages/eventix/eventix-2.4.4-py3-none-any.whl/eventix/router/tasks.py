import logging
from typing import Annotated

from fastapi import APIRouter, Body, Depends

from eventix.exceptions import NoTaskFound
from eventix.functions.task import task_next_scheduled, tasks_by_status, tasks_by_task, tasks_dump
from eventix.pydantic.pagination import dep_pagination_parameters, PaginationParametersModel
from eventix.pydantic.response_models import RouterTasksResponseModel
from eventix.pydantic.task import TaskModel

log = logging.getLogger(__name__)

router = APIRouter(tags=["tasks"])


@router.get("/tasks/next_scheduled")
async def route_tasks_next_scheduled_get(worker_id: str, namespace: str) -> TaskModel:
    t = task_next_scheduled(worker_id, namespace)
    if t is None:
        raise NoTaskFound(namespace=namespace)
    return t


@router.put("/tasks/by_status")
async def router_tasks_by_status_put(
    status: Annotated[str, Body()] = None,
    namespace: Annotated[str, Body()] = None,
    pagination: PaginationParametersModel = Depends(dep_pagination_parameters)
) -> RouterTasksResponseModel:
    data, max_results = tasks_by_status(
        status=status,
        namespace=namespace,
        pagination=pagination,
        max_results=True
    )
    return RouterTasksResponseModel(
        data=data,
        max_results=max_results,
        **pagination.model_dump()
    )


@router.put("/tasks/by_task")
async def router_tasks_by_task_put(
    task: Annotated[str, Body()],
    namespace: Annotated[str, Body()] = None,
    pagination: PaginationParametersModel = Depends(dep_pagination_parameters)
) -> RouterTasksResponseModel:
    data, max_results = tasks_by_task(
        task=task,
        namespace=namespace,
        pagination=pagination
    )
    return RouterTasksResponseModel(
        data=data,
        max_results=max_results,
        **pagination.model_dump()
    )

@router.put("/tasks/dump")
async def router_tasks_uids(
    # task: Annotated[str, Body()],
    # namespace: Annotated[str, Body()] = None,
    pagination: PaginationParametersModel = Depends(dep_pagination_parameters)
) -> RouterTasksResponseModel:
    data = tasks_dump(
        # task=task,
        # namespace=namespace,
        pagination=pagination
    )
    return RouterTasksResponseModel(
        data=data,
        max_results=0,
        **pagination.model_dump()
    )
