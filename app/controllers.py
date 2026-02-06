from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy import select
from .schemas import BookCreate
from .models import Book
def create_book_controller(db: Session,the_book: BookCreate ):
    try:

        query = select(Book).where(Book.isbn==the_book.isbn)
        existing_book = db.scalar(query)

        if existing_book:
            raise HTTPException(status_code=409, detail="Book already exists")
        
        new_book = Book(**the_book.model_dump())
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book
    except SQLAlchemyError as e:
        raise e
    except Exception as e:
        raise e