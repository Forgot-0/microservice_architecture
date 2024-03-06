from typing import List, Tuple
from fastapi import APIRouter, Depends
from api.deps import bookmark_service, like_service, dislike_service
from schemas.reaction import Reaction
from schemas.totalreaction import TotalReaction
from schemas.bookmark import IsBookmark, AvgBookmark, Bookmark



router = APIRouter()


@router.get('/get_all_info/', response_model=List[Tuple[Reaction | Bookmark | None, TotalReaction | AvgBookmark | None]])
async def get_all_infos(bookmarks: bookmark_service, likes: like_service, dislike: dislike_service, info: IsBookmark = Depends()):
    res = await bookmarks.get_all_info(info)
    res = [await likes.get_all_info(info), await dislike.get_all_info(info)] + [res]
    return res
