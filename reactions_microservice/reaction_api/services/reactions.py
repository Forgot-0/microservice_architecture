from repositories.reaction import ReactionRepository
from repositories.totalreaction import TotalReactionRepository
from bson import ObjectId
from schemas.reaction import Reaction, ReactionByType, IsReaction
from typing import List




class ReactionService:
    def __init__(self, reaction: ReactionRepository, totalreaction: TotalReactionRepository) -> None:
        self.reaction = reaction
        self.totalreaction = totalreaction

    async def create(self, reaction: Reaction):
        reaction = reaction.model_dump()

        res = await self.reaction.create(reaction)
        await self.totalreaction.create_or_update(
            {'object_type':reaction['object_type'],
            'object_pk':reaction['object_pk']})

        return res

    async def delete_by_id(self, id: ObjectId):
        reaction = await self.reaction.get_by_id(id)

        res = await self.reaction.delete_by_id(id)
        await self.totalreaction.create_or_update(
            {'object_type':reaction['object_type'],
            'object_pk':reaction['object_pk']}, -1)
        return res

    async def get_by_id(self, id: ObjectId) -> Reaction:
        res = await self.reaction.get_by_id(id)
        return res

    async def get_is_reaction(self, is_react: IsReaction) -> Reaction:
        res = await self.reaction.get_is_reaction(is_react.model_dump())
        return res

    async def find(self, filter: dict) -> List[Reaction]:
        res = await self.reaction.find(filter)
        return res
    
    async def get_by_type(self, type: ReactionByType) -> List[Reaction]:
        res = await self.reaction.get_by_type(type.model_dump())
        return res
    
    async def get_all_info(self, react: IsReaction):
        params = react.model_dump()
        is_react = await self.reaction.get_is_reaction(params)
        params.pop('user_id')
        total_react = await self.totalreaction.get(params)
        return [is_react, total_react]