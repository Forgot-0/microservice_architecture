from schemas.utils import PaginateParams
from repositories.bookmark import BookmarkRepository
from repositories.totalreaction import TotalReactionRepository
from bson import ObjectId
from schemas.bookmark import AvgBookmark, Bookmark, IsBookmark, CreateBookmark, GetAvgBookmark
from typing import List



class BookmarkService:
    def __init__(self, bookmark: BookmarkRepository) -> None:
        self.bookmark = bookmark

    async def create(self, bookmark: CreateBookmark):
        res = await self.bookmark.create(bookmark.model_dump())
        return res
    
    async def delete_by_id(self, id: ObjectId):
        res = await self.bookmark.delete_by_id(id)
        return res
    
    async def get_is_bookmark(self, is_bookmark: IsBookmark) -> Bookmark:
        res = await self.bookmark.get_is_bookmark(is_bookmark.model_dump())
        return res
    
    async def get_avg_bookmark(self, avg_bookmark:GetAvgBookmark) -> List[AvgBookmark]:
        res = await self.bookmark.get_aggregate(await self.get_rating_aggregation(**avg_bookmark.model_dump()))
        return res

    async def get_avg_many_bookmark(self, params: PaginateParams, sort: int = 1) -> List[AvgBookmark]:
        object_type, page, size = params.model_dump().values()
        res = await self.bookmark.get_aggregate(await self.get_rating_many(object_type, sort, page, size))

        return res
    
    async def get_all_info(self, bookmark: IsBookmark):
        params = bookmark.model_dump()

        is_react = await self.bookmark.get_is_bookmark(params)
        params.pop('user_id')
        avg_bookmark = await self.bookmark.get_aggregate(await self.get_rating_aggregation(**params))
        return [is_react, avg_bookmark[0] if avg_bookmark else None]



    async def get_rating_aggregation(self, object_pk: int, object_type: str, sort=-1):
        aggregation_rating = [

            {
                "$match": {
                    "object_pk": object_pk, 
                    "object_type": object_type
                    }
            },
            {
                "$group": {
                    "_id": {
                        "object_pk": "$object_pk",
                        "object_type": "$object_type",
                       
                    },
                    "rating": {"$avg": "$value"}
                }
            },
            {
                "$project": {
                    "object_pk": "$_id.object_pk",
                    "object_type": "$_id.object_type",
                    "rating": 1,
                    "_id": 0
                }
            },
        ]
        return aggregation_rating
    

    async def get_rating_many(self, object_type: str, sort: int = -1, page: int = 0, size: int = 20):
        aggregation_rating_many = [
            {
                "$match": {"object_type": object_type}
            },
            {
                "$group": {
                    "_id": {
                        "object_pk": "$object_pk",
                        "object_type": "$object_type",
                    },
                    "rating": {"$avg": "$value"}
                }
            },
            {
                "$project": {
                    "object_pk": "$_id.object_pk",
                    "object_type": "$_id.object_type",
                    "rating": 1,
                    "_id": 0
                }
            },
            {
                "$sort": {
                    "rating": sort
                }
            },
            {
                "$skip": page*size
            },
            {
                "$limit": size
            },
        ]
        return aggregation_rating_many
