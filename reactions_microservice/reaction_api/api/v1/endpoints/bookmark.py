from typing import List, Tuple
from fastapi import APIRouter, Depends, Body
from api.deps import bookmark_service
from schemas.bookmark import CreateBookmark, IsBookmark, AvgBookmark, PyObjectId, Bookmark, GetAvgBookmark
from schemas.utils import PaginateParams


router = APIRouter()


@router.post('/create_bookmark/')
async def create_bookmark(bookmarks: bookmark_service, bookmark: CreateBookmark = Body()):
    res = await bookmarks.create(bookmark)
    return res


@router.get('/is_bookmark/', response_model=Bookmark)
async def get_is_bookmark(bookmarks: bookmark_service, is_bookmark: IsBookmark = Depends()):
    res = await bookmarks.get_is_bookmark(is_bookmark)
    return res


@router.delete('/delete_bookmark/')
async def delete_bookmark(bookmarks: bookmark_service, id: PyObjectId):
    res = await bookmarks.delete_by_id(id)
    return res


@router.get('/get_avg_bookmark/', response_model=List[AvgBookmark])
async def get_bookmark(bookmarks: bookmark_service, bookmark: GetAvgBookmark = Depends()):
    res = await bookmarks.get_avg_bookmark(bookmark)
    return res


@router.get('/get_by_bookmark/', response_model=List[AvgBookmark])
async def get_by_bookmark(bookmarks: bookmark_service, params: PaginateParams = Depends(), sort: int = -1):
    res = await bookmarks.get_avg_many_bookmark(params, sort)
    return res


