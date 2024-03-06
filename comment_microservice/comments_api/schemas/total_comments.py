from pydantic import BaseModel


class TotalComments(BaseModel):
    object_pk: int
    object_type: str
    total: int


class SearchTotal(BaseModel):
    object_type: str
    object_pk: str