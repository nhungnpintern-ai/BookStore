from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models.book import Book
from Schema.book import BookCreate, BookResponse
from database import get_db

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("", response_model=BookResponse, status_code=201)
def create_Book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.get("", response_model=List[BookResponse])
def ListBooks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Book).offset(skip).limit(limit).all()


@router.get("/{books_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{books_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    ud_book = db.query(Book).filter(Book.id == book_id).first()
    if not ud_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.model_dump().items():
        setattr(ud_book, key, value)
    db.commit()
    db.refresh(ud_book)
    return ud_book


@router.delete("/{books_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    db.delete(book)
    db.commit()
