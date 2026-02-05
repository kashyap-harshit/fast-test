from fastapi import FastAPI, Request
import time


app = FastAPI()



@app.get("/")
async def home():
    return "this is home"


@app.middleware("http")
async def the_middleware(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers['custom-header'] = 'harshit is here'
    return response


