from math import ceil
from motor.core import AgnosticCollection, AgnosticCursor
from schemas.totalreaction import TotalReaction


class TotalReactionRepository:

    def __init__(self, collection: AgnosticCollection) -> None:
        self.collection = collection

    async def create_or_update(self, total_reaction: dict, inc: int=1) -> None:
        res = await self.collection.find_one_and_update(
        total_reaction,
        {"$inc": {"total": inc}},
        upsert=True,
        return_document=False)
        return res

    async def get(self, total_reaction: dict) -> TotalReaction:
        res = await self.collection.find_one(total_reaction)
        return res

    async def orber_by_total(self, object_type) -> AgnosticCursor:
        projection = {'_id': 0, 'object_pk': 1, 'total': 1, 'object_type': 1}
        res = self.collection.find(
            {'object_type': object_type}, 
            projection=projection
            ).sort({'total' : 1})
        return res

    async def paginate(self, filters: dict, sort: dict, page: int = 0, size: int = 20):

        total_document = await self.collection.estimated_document_count()

        res = await self.collection.find(filters).sort(sort).skip(page*size).limit(size).to_list(length=None)
        count_page = ceil(total_document/size)

        return {
            'items': res,
            'paginate_info':{
                'total': total_document, 
                'pages': count_page,
                'prev': page > 0,
                'next': page < count_page-1,
            }
        }










