from typing import List

from eventix.pydantic.pagination import PaginationResultModel
from eventix.pydantic.task import TaskModel


class RouterTasksResponseModel(PaginationResultModel):
    data: List[TaskModel]
