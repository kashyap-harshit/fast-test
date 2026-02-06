from sqlalchemy import Column, Integer, Row, String, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship

from .database import DeclarativeBase

    

class Shelf(DeclarativeBase):
    __tablename__="shelves"
    id=Column(Integer, nullable=False, index=True, primary_key=True)
    size_of_shelf = Column(Enum("big", "small", name="shelf_size"), nullable=False)


    def __repr__(self):
        return f"<ItemModel(shelf_id={self.id}, size_of_shelf={self.size_of_shelf})>"

class Book(DeclarativeBase):
    __tablename__ = "books"
    isbn = Column(Integer, primary_key=True, index=True)
    book_name=Column(String(80), nullable=False, unique=True)
    author_name=Column(String(80), nullable=False, unique=False)
    no_of_pages = Column(Integer, nullable=True)
    shelf_id = Column(Integer, ForeignKey("shelves.id"), nullable=False)
    print_type = Column(Enum("hardcover", "paperback", name="print_types"))
    price =Column(Float, nullable=False)

    def __repr__(self):
        return f"<ItemModel(book_name={self.book_name}, author_name={self.author_name}, price={self.price})>"
