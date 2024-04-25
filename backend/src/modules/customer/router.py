from fastapi import APIRouter
from typing import List, Dict

customer_router = APIRouter(
    prefix="/customer",
    tags=['Customer']
)

@customer_router.get('/')
async def customer() -> List[Dict]:
    return [ {'name': f"customer-{str(i)}"} for i in range(200) ]