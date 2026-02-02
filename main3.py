from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {200, "backend is up and running"}

fake_data = [{"item1": "apple"}, {"item2": "banana"}, {"item3": "carrrot"}]

@app.get("/items")
async def get_item(skip: int = 0, limit: int = 10):
    return fake_data[skip: skip + limit]

@app.get("/things/{item_id}")
async def get_thing(item_id, q: str | None = None, short: bool = False):
    if q:
        return {"msg": f"yaay you gave q: {q}"}
    if not short:
        return {"msg": "daayem this is not short very tall"}
    return {"msg": "normal"}