from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {200, "backend is up and running"}

fake_data = [{"item1": "apple"}, {"item2": "banana"}, {"item3": "carrrot"}]

@app.get("/items")
async def get_item(skip: int = 0, limit: int = 10):
    return fake_data[skip: skip + limit]

@app.get("/things")
async def get_things(lmao: str):
    return {"value of lmao": lmao}