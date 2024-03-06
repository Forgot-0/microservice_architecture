from typing import List
from fastapi import APIRouter, Depends, Query, Body
from schemas.comments import Comment, CreateComment, PyObjectId, PaginationComments, SearchComment
from api.deps import comment_service
from cache import cache

router = APIRouter()


@router.get('/get_comments/', response_model=PaginationComments | str)
async def get_comments(comments: comment_service, comment: SearchComment = Depends(), page: int = 0, size: int = 20):
    res = await comments.paginate(comment.model_dump(), {}, page, size)
    return res


@router.get('/get_comments_by_id/', response_model=List[Comment])
async def get_comments_by_ids(commets: comment_service, spisok_id: List[PyObjectId] = Query(...)):
    res = await commets.get_more_by_id(spisok_id)
    return res


@router.post('/create_comment/', include_in_schema=True)
async def create_comment(comments: comment_service, comment:CreateComment = Body()):
    res = await comments.save(comment)
    return res.acknowledged


@router.delete('/delete_comment/')
async def delete_comment(id:PyObjectId, comments: comment_service):
    res = await comments.delete_by_id(id)
    return res.raw_result


@router.patch('/update_comment/')
async def update_comment(comments: comment_service, comment: Comment = Body()):
    res = await comments.update(comment)
    return res.raw_result