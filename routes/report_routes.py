from fastapi import APIRouter, HTTPException
from database import book_db, member_db
from logs.logger_config import get_logger

logger = get_logger(__name__)

router = APIRouter()
book = book_db.BookDB()
member = member_db.MemberDB()

@router.get("/summary")
def count_all_books():
    return f"count_total_books: {book.count_total_books()[0]},\
        count_available_books: {book.count_available_books()[0]},\
            count_borrowed_books: {book.count_borrowed_books()[0]}"

@router.get("/books-by-genre")
def count_by_genre(genre):
    return book.count_books_by_genre(genre)

@router.get("/summary")
def count_active_members():
    pass

@router.get("/top-member")
def get_top_member():
    try:
        return member.get_top_member()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")