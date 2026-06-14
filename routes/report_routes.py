from fastapi import APIRouter, HTTPException
from database import book_db
from logs.logger_config import get_logger

logger = get_logger(__name__)

router = APIRouter()
book = book_db.BookDB()

@router.get("/summary")
def count_all_books():
    return book.count_total_books()

@router.get("/books-by-genre")
def count_by_genre(genre):
    return book.count_books_by_genre(genre)