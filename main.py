from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "new world, new day, new life"}







