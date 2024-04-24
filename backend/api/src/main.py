from fastapi import FastAPI

app = FastAPI()


@app.get('/health')
async def health():
    return {
        "status": 200,
        "message": "Everything is ok"
    }

@app.get('/test')
async def test():
    return {
        "status": 200,
        "message": "Test"
    }