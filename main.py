from fastapi import FastAPI
from core.database import engine, Base
from routers.book import router as book_router
from core.config import PROJECT_NAME, PROJECT_VERSION
from models import book

Base.metadata.create_all(bind=engine)

app = FastAPI(title=PROJECT_NAME, version=PROJECT_VERSION)
app.include_router(book_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Beginner Project! "}
