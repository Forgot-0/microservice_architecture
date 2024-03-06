from fastapi import APIRouter
from api.v1.endpoints import comments, total_comments

routers = APIRouter()
router_list = [comments.router, total_comments.router]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)