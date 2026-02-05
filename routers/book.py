from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


from core.database import get_db
from schema.book import BookCreate, BookUpdate, BookResponse
from crud import book as crud
from models.book import Book
from core.deps import get_current_user, get_current_admin_user

router = APIRouter(prefix="/book", tags=["Books"])


@router.post("", response_model=BookResponse, status_code=201)
def create_book(
    book: BookCreate, db: Session = Depends(get_db), user=Depends(get_current_user)
):
    return crud.create_book(db, book, owner_id=user.id)


@router.get("", response_model=List[BookResponse])
def list_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.list_books(db, skip, limit)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book: BookUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    updated = crud.update_book(db, book_id, book, user.id)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated


@router.delete("/{book_id}", status_code=204)
def delete_book(
    book_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin_user)
):
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
