from database import Base
from sqlalchemy import Column, Integer, String, Float, Date
from typing import Optional


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    published_date = Column(Date, nullable=True)
