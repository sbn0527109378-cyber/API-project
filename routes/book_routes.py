from fastapi import APIRouter, HTTPException
from database import book_db
from pydantic_classes import books
from logs.logger_config import get_logger

logger = get_logger(__name__)

router = APIRouter()
book = book_db.BookDB()

@router.post("/")
def create_book(data: books.Book):
    return book.create_book(data.__dict__)

