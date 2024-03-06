from typing import Annotated
from fastapi import Depends
from models.database import likes, total_likes, dislikes, total_dislikes, bookmarks

from repositories.reaction import ReactionRepository
from services.reactions import ReactionService

from repositories.totalreaction import TotalReactionRepository
from services.totalreaction import TotalReactionService

from repositories.bookmark import BookmarkRepository
from services.bookmark import BookmarkService



def get_like_service() -> ReactionService:
    total = TotalReactionRepository(total_likes)
    like_service = ReactionService(ReactionRepository(likes), total)
    return like_service

def get_dislike_service() -> ReactionRepository:
    total = TotalReactionRepository(total_dislikes)
    dislike_service = ReactionService(ReactionRepository(dislikes), total)
    return dislike_service

def get_total_like_service() -> TotalReactionService:
    total_like_service = TotalReactionService(TotalReactionRepository(total_likes))
    return total_like_service

def get_total_dislike_service() -> TotalReactionService:
    total_dislike_service = TotalReactionService(TotalReactionRepository(total_dislikes))
    return total_dislike_service

def get_bookmark_service() -> BookmarkService:
    return BookmarkService(BookmarkRepository(bookmarks))


like_service = Annotated[ReactionService, Depends(get_like_service)]
dislike_service = Annotated[ReactionService, Depends(get_dislike_service)]

total_like_service = Annotated[TotalReactionService, Depends(get_total_like_service)]
total_dislike_service = Annotated[TotalReactionService, Depends(get_total_dislike_service)]


bookmark_service = Annotated[BookmarkService, Depends(get_bookmark_service)]