from fastapi import FastAPI
from pydantic import BaseModel



class Item(BaseModel):
    name: str
    desc: str
    price: int | None = None
    tax: int | None = None

app = FastAPI()


@app.post("/here")
async def handle_here(item: Item):
    return {"msg": item.model_dump()}