import logging
from typing import Annotated

from fastapi import APIRouter, Body, Depends

from eventix.exceptions import NoTaskFound
from eventix.functions.task import task_next_scheduled, tasks_by_status, tasks_by_task
from eventix.pydantic.namespaces import NamespacesResponseModel, NamespaceTaskTypesResponseModel
from eventix.pydantic.pagination import dep_pagination_parameters, PaginationParametersModel
from eventix.pydantic.response_models import RouterTasksResponseModel
from eventix.pydantic.task import TaskModel

log = logging.getLogger(__name__)

router = APIRouter(tags=["tasks"])


@router.get("/namespaces")
async def router_namespaces_get() -> NamespacesResponseModel:
    raise NotImplementedError()
    # return NamespacesResponseModel(namespaces=[])


@router.get("/namespace/{namespace}/task_types")
async def router_namespace_task_types_get(
    namespace: str,
) -> NamespaceTaskTypesResponseModel:
    raise NotImplementedError()
    # return NamespaceTaskTypesResponseModel(task_types=[])
