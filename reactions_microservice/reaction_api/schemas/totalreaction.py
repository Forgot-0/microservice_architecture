from pydantic import BaseModel
from typing import List
from .utils import Pagination

class TotalReaction(BaseModel):
    object_type: str
    object_pk: str
    total: int


class GetTotalReaction(BaseModel):
    object_type: str
    object_pk: str


class TotalPagination(BaseModel):
    items: List[TotalReaction]
    paginate_info: Pagination