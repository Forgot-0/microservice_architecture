from typing import List, Tuple
from fastapi import APIRouter, Depends, Body
from api.deps import like_service, dislike_service
from schemas.reaction import CreateReaction, IsReaction, Reaction, PyObjectId
from schemas.totalreaction import TotalReaction


router = APIRouter()


@router.post('/reaction/', response_model=bool)
async def create_like(likes: like_service, dislikes: dislike_service, like: CreateReaction = Body(), reac: bool = True):
    if  reac:
        res = await likes.create(like)

    res = await dislikes.create(like)
    return res

@router.get('/is_react/', response_model=Reaction)
async def get_reaction(likes: like_service, dislike: dislike_service, reaction: IsReaction = Depends()):
    return await likes.get_is_reaction(reaction) or await dislike.get_is_reaction(reaction)

@router.delete('/unreaction/', response_model=dict)
async def delete_reaction(likes: like_service, dislike: dislike_service, id: PyObjectId):
    return await likes.delete_by_id(id) or await dislike.delete_by_id(id)
