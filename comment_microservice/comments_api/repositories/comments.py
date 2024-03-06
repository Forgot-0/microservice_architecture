from datetime import datetime
from motor.core import AgnosticCollection
from bson import ObjectId
from schemas.comments import Comment
from typing import List

class CommentRepository:

    def __init__(self, collection: AgnosticCollection) -> None:
        self.collection = collection

    async def create(self, comment: dict):
        date = datetime.utcnow()
        res = await self.collection.insert_one({**comment, 'date_create':date, 'date_update':date})
        return res

    async def find(self, comment: dict) -> List[Comment]:
        res = await self.collection.find(comment).to_list(length=None)
        return res

    async def get_by_id(self, id: ObjectId) -> Comment:
        res = await self.collection.find_one({'_id': id})
        return res
    
    async def get_more_by_id(self, spisok_id = List[ObjectId]):
        res = await self.collection.find({"_id": {"$in": spisok_id}}).to_list(length=None)
        return res

    async def update(self, comment: dict):
        _id = ObjectId(comment.pop('id'))
        update_data = {
            "$set": {**comment, 'date_update': datetime.utcnow()}
        }
        res = await self.collection.update_one({'_id': _id}, update=update_data)
        return res

    async def delete_by_id(self, id: ObjectId):
        res = await self.collection.delete_one({'_id': id})
        return res
    
    async def paginate(self, filter: dict, sort: dict, page: int, size: int) -> List[Comment]:

        collect = self.collection.find(filter)
        if sort:
            collect = collect.sort(sort)

        res = await collect.skip(page*size).limit(size).to_list(length=None)
        return res