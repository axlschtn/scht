from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def health():
    return "Super Cool"

@app.get('/test')
async def test():
    return "TEST"

@app.get('/axel')
async def test():
    return "axel"

@app.get('/abcd')
async def test():
    return "axel"