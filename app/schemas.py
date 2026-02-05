from pydantic import BaseModel


class BookCreate(BaseModel):
    id: str
    