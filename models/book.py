from core.database import Base
from sqlalchemy import Column, Integer, String, Float, Date, CheckConstraint, ForeignKey
from typing import Optional
from sqlalchemy.orm import relationship
from models.user import User


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Float, CheckConstraint("price > 0"), nullable=False)
    published_date = Column(Date, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User")
