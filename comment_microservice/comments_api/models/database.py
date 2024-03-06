import motor.motor_asyncio
import asyncio


MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client['comments']

comments = database['comment_collections'] #
total_comments = database['total_comment_collections'] #


async def create_index_comments():
    index_keys_co = [("object_type", 1), ("object_pk", 1)]

    index_options_co = {
        "name": "co",
        "unique": True,
        "background": True
    }

    await comments.create_index(index_keys_co, **index_options_co)



async def create_index_total_comments():
    index_keys_co = [("object_type", 1), ("object_pk", 1)]

    index_options_co = {
        "name": "co",
        "unique": True,
        "background": True
    }

    await total_comments.create_index(index_keys_co, **index_options_co)


async def create_indexs():
    await create_index_comments()
    await create_index_total_comments()


if __name__ == '__main__':
    asyncio.run(create_indexs())