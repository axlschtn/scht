from fastapi import APIRouter
from typing import List, Dict

user_router = APIRouter(
    prefix="/users",
    tags=['User']
)

@user_router.get('/')
async def users() -> List[Dict]:
    return [ {'name': f"name-{str(i)}"} for i in range(10) ]