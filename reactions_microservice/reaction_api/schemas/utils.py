from pydantic import ValidationInfo, BaseModel
from bson import ObjectId
from bson.errors import InvalidId
from pydantic_core import core_schema
from pydantic_core.core_schema import str_schema





class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, _: ValidationInfo):
        if isinstance(v, bytes):
            v = v.decode("utf-8")
        try:
            return PyObjectId(v)
        except InvalidId:
            raise ValueError("Id must be of type PydanticObjectId")

    @classmethod
    def __get_pydantic_json_schema__(
        cls, schema, handler
    ):
        json_schema = handler(schema)
        json_schema.update(
            type="string",
            example="5eb7cf5a86d9755df3a6c593",
        )
        return json_schema

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type, handler
    ):
        return core_schema.json_or_python_schema(
            python_schema=core_schema.with_info_plain_validator_function(
                cls.validate
            ),
            json_schema=str_schema(),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda instance: str(instance)
            ),
        )


class Pagination(BaseModel):
    total: int
    pages: int
    prev: bool
    next: bool


class PaginateParams(BaseModel):
    object_type: str
    page: int = 0
    size: int = 20


class Object(BaseModel):
    object_type: str
    object_pk: str



