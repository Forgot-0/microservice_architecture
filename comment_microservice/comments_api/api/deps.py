from typing import Annotated
from fastapi import Depends
from models.database import comments, total_comments

from repositories.comments import CommentRepository
from services.comments import CommentsService

from repositories.total_comments import TotalCommentRepository
from services.total_comments import TotalCommentsService



async def get_comment_service() -> CommentsService:
    total_repo = TotalCommentRepository(total_comments)
    comment_service = CommentsService(CommentRepository(comments), total_repo)
    return comment_service


async def get_total_sevice() -> TotalCommentsService:
    total_service = TotalCommentsService(TotalCommentRepository(total_comments))
    return total_service



comment_service = Annotated[CommentsService, Depends(get_comment_service)]
total_service = Annotated[TotalCommentsService, Depends(get_total_sevice)]