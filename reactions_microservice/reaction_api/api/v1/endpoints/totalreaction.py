from fastapi import APIRouter, Depends
from api.deps import total_like_service, total_dislike_service
from schemas.totalreaction import TotalReaction, GetTotalReaction, TotalPagination
from schemas.utils import PaginateParams
from typing import List

router = APIRouter()



@router.get('/get_total/', response_model=List[TotalReaction | None])
async def get_total(totallikes: total_like_service, totaldislikes: total_dislike_service, totalreaction: GetTotalReaction = Depends()):
    return ([await totallikes.get(totalreaction), await totaldislikes.get(totalreaction)])


@router.get('/by_popular/', response_model=TotalPagination)
async def get_by_popular(total_service: total_like_service, parametrs: PaginateParams = Depends()):
    res = await total_service.get_popular(parametrs)
    return res
