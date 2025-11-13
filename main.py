from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "from new2 branch"}







