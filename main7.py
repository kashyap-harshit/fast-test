from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
app = FastAPI()


items = {"foo": "this item is foo"}


@app.get("/")
async def home():
    return "backend is up and running"



@app.get("/items/{item_name}")
async def get_item(item_name: str):
    if item_name not in items:
        raise HTTPException(status_code=404, detail=['item', 'not', 'fouond'])
    return {"item": items[item_name]}



@app.get("/try_json")
async def try_json():
    return JSONResponse(status_code=201, content={"this": "is the content"})


class CustomWebException(Exception):
    def __init__(self, name:str):
        self.name = name

@app.exception_handler(CustomWebException)
async def custom_web_exception_handler(request:Request, exc: CustomWebException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something, there goes a rainbow..."}
    )

@app.get("/custom/{name}")
async def get_custom(name: str):
    if name=="hey":
        return "yes that is a valid hey"
    else:
        raise CustomWebException(name="fastapi")