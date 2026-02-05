from fastapi import FastAPI, HTTPException
app = FastAPI()


items = {"foo": "this item is foo"}


@app.get("/")
async def home():
    return "backend is up and running"



@app.get("/items/{item_name}")
async def get_item(item_name: str):
    if item_name not in items:
        raise HTTPException(status_code=404, detail="item not found mate")
    return {"item": items[item_name]}