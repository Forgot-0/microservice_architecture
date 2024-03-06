import motor.motor_asyncio
import asyncio

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client['reactions']

likes = database['like_collections']
dislikes = database['dislike_collections']
bookmarks = database['bookmark_collections']
total_likes = database['total_like_collections']
total_dislikes = database['total_dislike_collections']



if __name__ == '__main__':
    # asyncio.run(main())
    pass