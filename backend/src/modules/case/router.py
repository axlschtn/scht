from typing import List, Dict
from fastapi import APIRouter

case_router = APIRouter(
    prefix='/cases',
    tags=['Case']
)

@case_router.get('/')
async def cases() -> List[Dict]:
    return [ {'name': f"case-{str(i)}"} for i in range(200) ]