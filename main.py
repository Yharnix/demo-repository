from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "From the new1 branch"}







