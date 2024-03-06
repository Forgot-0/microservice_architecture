from typing import List
from fastapi import APIRouter, Depends
from schemas.total_comments import SearchTotal, TotalComments
from api.deps import total_service
from cache import cache

router = APIRouter()


@router.get('/get_total_comments/', response_model=TotalComments | None)
async def get_total_comments(total_comments: total_service, total: SearchTotal = Depends()):
    res = await total_comments.get(total)
    return res