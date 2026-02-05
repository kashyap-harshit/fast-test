from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()



origins = [
    'http://localhost:3000',
    'https://google.com'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET'],
    allow_headers=['*']
)

@app.get("/")
async def home():
    return {"message": "backend is up and running"}