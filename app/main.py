from fastapi import FastAPI, Depends
from app.schemas import BookCreate
from app.database import get_db
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/")
async def home():
    return "backend is up"



@app.post("/create_book")
async def create_book(the_book: BookCreate, db : Session= Depends(get_db)):
    return {"message": f"the book has been created: {the_book} {db}"}