from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class BookBase(BaseModel):
    title: str
    author: str
    price: float
    published_date: Optional[date] = None


class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    published_date: date


class BookResponse(BookBase):
    id: int
    price: float

    class Config:
        from_attributes = True


class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    published_date: Optional[date] = None
