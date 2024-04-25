from fastapi import FastAPI
from modules.customer.router import customer_router
from modules.users.router import user_router
from modules.case.router import case_router

app = FastAPI()

app.include_router(customer_router)
app.include_router(user_router)
app.include_router(case_router)


@app.get('/')
async def health():
    return "Super Cool"