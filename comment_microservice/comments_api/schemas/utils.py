from pydantic import BaseModel



class Pagination(BaseModel):
    total: int
    pages: int
    prev: bool
    next: bool


class PaginateParams(BaseModel):
    page: int = 0
    size: int = 10