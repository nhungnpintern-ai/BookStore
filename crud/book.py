from sqlalchemy.orm import Session
from models.book import Book
from schema.book import BookCreate, BookUpdate


def create_book(db: Session, book: BookCreate) -> Book:
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def list_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book(db: Session, book_id=int) -> Book | None:
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(db: Session, book_id: int, book: BookUpdate) -> Book | None:
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        return None
    for key, value in book.model_dump(exclude_unset=True).items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int) -> Book | None:
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        return None

    db.delete(db_book)
    db.commit()
    return db_book
