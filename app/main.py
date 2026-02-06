from fastapi import FastAPI, Depends, HTTPException
from app.schemas import BookCreate
from app.database import get_db
from sqlalchemy.orm import Session
from .controllers import create_book_controller

app = FastAPI()


@app.get("/")
async def home():
    return "backend is up"



@app.post("/create_book")
async def create_book(the_book: BookCreate, db : Session= Depends(get_db)):
    book =  create_book_controller(db, the_book=the_book)
    if book:

        return {"message": f"the book has been created: {book} {db}"}
    return HTTPException(500, detail="book not found")