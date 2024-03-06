from motor.core import AgnosticCollection
from schemas.total_comments import TotalComments


class TotalCommentRepository:
    
    def __init__(self, collection: AgnosticCollection) -> None:
        self.collection = collection

    async def create_or_update(self, total_comment: dict, inc: int=1):
        res = await self.collection.find_one_and_update(
        total_comment,
        {"$inc": {"total": inc}},
        upsert=True,
        return_document=False)
        return res

    async def get(self, total_comment: dict) -> TotalComments:
        res = await self.collection.find_one(total_comment)
        return res