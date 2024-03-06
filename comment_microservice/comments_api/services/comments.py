from typing import List
from schemas.comments import Comment, CreateComment, PaginationComments, SearchComment
from repositories.comments import CommentRepository
from repositories.total_comments import TotalCommentRepository
from bson import ObjectId
from math import ceil



class CommentsService:
    def __init__(self, comment_repository: CommentRepository, total_comment_repository: TotalCommentRepository) -> None:
        self.comment_repository = comment_repository
        self.total_comment_repository = total_comment_repository

    async def save(self, comment: CreateComment):
        comment = comment.model_dump()

        res = await self.comment_repository.create(comment)
        await self.total_comment_repository.create_or_update(
            {'object_type':comment['object_type'],
            'object_pk':comment['object_pk']})
        return res
    
    async def get(self, id: ObjectId) -> Comment:
        res = await self.comment_repository.get_by_id(id)
        return res

    async def find(self, comment: SearchComment) -> PaginationComments:
        comment = comment.model_dump()
        res = await self.comment_repository.find(
            {'object_type': comment['object_type'],
            'object_pk': comment['object_pk']})
        
        return res

    async def update(self, comment: Comment):
        res = await self.comment_repository.update(comment.model_dump())
        return res
    
    async def delete_by_id(self, id: ObjectId):
        comment = await self.get(id)
        res = await self.comment_repository.delete_by_id(id)
        await self.total_comment_repository.create_or_update(
            {'object_type':comment['object_type'],
            'object_pk':comment['object_pk']}, -1)
        return res
    
    async def paginate(self, filter: dict, sort: dict, page: int, size: int) -> PaginationComments:
        res = await self.comment_repository.paginate(filter, sort, page, size)
        
        object_type, object_pk = filter.values()
        
        total = await self.total_comment_repository.get(
            {'object_type':object_type,
            'object_pk':object_pk})

        total = total['total'] if total else 0

        return {'comments': res,
                'paginate_info':{'total': total, 
                                'pages': ceil(total/size),
                                'prev': page > 0,
                                'next': (page+1)*size < total,
                            }
            }
    
    async def get_more_by_id(self, spisok_id = List[ObjectId]):
        res = await self.comment_repository.get_more_by_id(spisok_id)
        return res

        