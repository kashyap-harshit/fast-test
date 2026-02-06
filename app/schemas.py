from pydantic import BaseModel
from enum import Enum

class PrintType(str, Enum):
    paperback = 'paperback'
    hardcover = 'hardcover'


class BookCreate(BaseModel):
    isbn: str   
    book_name: str   
    author_name: str
    no_of_pages : int
    shelf_id    : int
    print_type  : PrintType
    price   : int