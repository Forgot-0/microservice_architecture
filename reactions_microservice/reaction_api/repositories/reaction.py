from typing import List
from motor.core import AgnosticCollection
from bson import ObjectId
from schemas.reaction import Reaction


class ReactionRepository:
    def __init__(self, collection: AgnosticCollection) -> None:
        self.collection = collection

    async def create(self, like: dict):
        res = await self.collection.insert_one(like)
        return res.acknowledged

    async def delete_by_id(self, id: ObjectId):
        res = await self.collection.delete_one({'_id': id})
        return res.raw_result

    async def get_by_id(self, id: ObjectId) -> Reaction:
        res = await self.collection.find_one({'_id': id})
        return res

    async def get_is_reaction(self, is_react: dict) -> Reaction:
        res = await self.collection.find_one(is_react)
        return res

    async def find(self, filter: dict) -> List[Reaction]:
        res = await self.collection.find(filter)
        return res
    
    async def get_by_type(self, type: dict) -> List[Reaction]:
        res = await self.collection.find(type)
        return res
