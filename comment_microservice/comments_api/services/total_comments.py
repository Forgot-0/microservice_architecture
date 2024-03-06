from repositories.total_comments import TotalCommentRepository
from schemas.total_comments import SearchTotal



class TotalCommentsService:
    def __init__(self, total_comment_repository: TotalCommentRepository):
        self.total_comment_repository: TotalCommentRepository = total_comment_repository

    async def get(self, total: SearchTotal):
        total = total.model_dump()
        res = await self.total_comment_repository.get(
            {'object_type': total['object_type'],
            'object_pk': total['object_pk']})
        return res
