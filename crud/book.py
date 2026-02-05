from sqlalchemy.orm import Session
from models.book import Book
from schema.book import BookCreate, BookUpdate


def create_book(db: Session, book: BookCreate, owner_id: int):
    db_book = Book(
        title=book.title,
        author=book.author,
        price=book.price,
        published_date=book.published_date,
        owner_id=owner_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def list_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int) -> Book | None:
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(
    db: Session,
    book_id: int,
    book_update: BookUpdate,
    user_id: int,
):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None

    update_data = {
        k: v
        for k, v in book_update.dict(exclude_unset=True).items()
        if v not in ("string", "", None)
    }

    for field, value in update_data.items():
        setattr(book, field, value)

    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: int) -> Book | None:
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        return None

    db.delete(db_book)
    db.commit()
    return db_book
