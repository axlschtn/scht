from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def health():
    return "Super Cool"

@app.get('/check')
async def health():
    return "Check"

@app.get('/check-bis')
async def health():
    return "Check-bis"

@app.get('/check-ter')
async def health():
    return "Check-ter"

@app.get('/check-quter')
async def health():
    return "Check-quter"