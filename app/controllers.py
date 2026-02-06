from sqlalchemy.orm import Session
from sqlalchemy import select
from .schemas import BookCreate
from .models import Book
def create_book_controller(db: Session,the_book: BookCreate ):
    query = select(Book).where(Book.isbn==the_book.isbn)
    existing_book = db.scalar(query)

    if existing_book:
        print(existing_book)
        return existing_book
    return ""