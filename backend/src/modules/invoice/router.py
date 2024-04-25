from fastapi import APIRouter
from typing import List, Dict

invoice_router = APIRouter(
    prefix="/invoice",
    tags=['Invoices']
)

@invoice_router.get('/')
async def invoices() -> List[Dict]:
    return [ {'name': f"invoice-{str(i)}"} for i in range(10) ]