from pydantic import BaseModel


class BookCreate(BaseModel):
    isbn: str   
    book_name: str   
    author_name: str
    no_of_pages : int
    shelf_id    : int
    print_type  : str
    price   : int