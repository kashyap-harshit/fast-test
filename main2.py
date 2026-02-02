from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def get_items(item_id: int):
    return {"Item": item_id}

from enum import Enum

class ModelName(str, Enum):
    this1 = "apple"
    this2 = "ball"
    this3 = "cat"

@app.get("/smt/{smt_txt}")
async def get_smt(smt_txt: ModelName):
    if smt_txt == ModelName.this1:
        return {"alpha name": f"{type(ModelName.this1.value)}", "message": "one apple a day keeps the doctor away"}
    if smt_txt.value == "ball":
        return {"alpha name": smt_txt, "message": "ball is good"}
    return {"alpha name": smt_txt, "message": "cats are the best"}


@app.get("/hello/1/{filepath:path}")
async def hey(filepath):
    return {"message": filepath}