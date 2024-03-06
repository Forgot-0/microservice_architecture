from math import ceil
from repositories.totalreaction import TotalReactionRepository
from schemas.totalreaction import GetTotalReaction
from schemas.utils import PaginateParams



class TotalReactionService:
    def __init__(self, total_reaction_repository: TotalReactionRepository):
        self.total_reaction_repository = total_reaction_repository

    async def get(self, total: GetTotalReaction):
        res = await self.total_reaction_repository.get(total.model_dump())
        return res
    
    async def get_popular(self, paramets: PaginateParams):
        object_type, page, size = paramets.model_dump().values()
        res = await self.total_reaction_repository.paginate({'object_type': object_type}, 
                                                            {'total': -1}, 
                                                            page,
                                                            size)
        return res
