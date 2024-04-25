from fastapi import APIRouter
from typing import List, Dict

case_router = APIRouter(
    prefix="/case",
    tags=['Case']
)

@case_router.get('/')
async def case() -> List[Dict]:
    return [ {'name': f"case-{str(i)}"} for i in range(50) ]