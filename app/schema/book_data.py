from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
import uuid


class CreateBook(BaseModel):
    title: str
    author: str
    published_date: date

class BookOut(BaseModel):
    status: bool = True
    message: str = "Successfully Created the Book"
    id: Optional[uuid.UUID]
    author: str
    published_date: date
    created_at: datetime
    class Config:
        orm_mode = True
