from fastapi import FastAPI
from api.v1.routers import routers

app = FastAPI()

app.include_router(routers)


# "object_type"='2' AND "comments"."object_pk"='324'