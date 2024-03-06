from math import ceil
from typing import List
from motor.core import AgnosticCollection, AgnosticCommandCursor
from bson import ObjectId
from schemas.bookmark import Bookmark


class BookmarkRepository:
    def __init__(self, collection: AgnosticCollection) -> None:
        self.collection = collection

    async def create(self, bookmark: dict):
        res = await self.collection.insert_one(bookmark)
        return res.acknowledged
    
    async def delete_by_id(self, id: ObjectId):
        res = await self.collection.delete_one({'_id': id})
        return res.raw_result

    async def get_aggregate(self, aggr: list):
        res = await self.collection.aggregate(aggr).to_list(length=None)
        return res

    async def get_is_bookmark(self, bookmark: dict) -> Bookmark:
        res = await self.collection.find_one(bookmark)
        return res

    async def find(self, aggregate: list):
        res = await self.collection.aggregate(aggregate).to_list(length=None)
        return res
    
    async def paginate(self, page, size):
        total_document = await self.collection.estimated_document_count()
        count_page = ceil(total_document/size)

        return {
            'paginate_info':{
                'total': total_document, 
                'pages': count_page,
                'prev': page > 0,
                'next': page < count_page-1,
            }
        }
