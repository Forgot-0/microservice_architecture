from datetime import datetime
from pydantic import BaseModel, Field
from .utils import PyObjectId





class Reaction(BaseModel):
    id: PyObjectId = Field(alias="_id")
    user_id: int
    object_type: str
    object_pk: str
    date_create: datetime


class CreateReaction(BaseModel):
    user_id: int
    object_type: str
    object_pk: str
    date_create: datetime = datetime.utcnow()


class IsReaction(BaseModel):
    user_id: int
    object_type: str
    object_pk: str


class ReactionByType(BaseModel):
    user_id: int
    object_type: str