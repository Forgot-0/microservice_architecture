from typing import List
from pydantic import BaseModel, Field
from .utils import Pagination, PyObjectId




class Bookmark(BaseModel):
    id: PyObjectId = Field(alias="_id")
    user_id: int
    object_type: str
    object_pk: str
    value: int


class CreateBookmark(BaseModel):
    user_id: int
    object_type: str
    object_pk: str
    value: int



class IsBookmark(BaseModel):
    user_id: int
    object_type: str
    object_pk: str


class GetAvgBookmark(BaseModel):
    object_type: str
    object_pk: str


class AvgBookmark(BaseModel):
    rating: float
    object_type: str
    object_pk: str

