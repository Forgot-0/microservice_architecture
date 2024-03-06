from fastapi import APIRouter
from api.v1.endpoints import reaction, totalreaction, bookmark, all_info

routers = APIRouter()
router_list = [reaction.router, totalreaction.router, bookmark.router, all_info.router]

for router in router_list:
    # router.tags = routers.tags.append("v1")
    routers.include_router(router)