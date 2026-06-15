from fastapi import APIRouter, HTTPException
from database import book_db
from pydantic_classes import books
from logs.logger_config import get_logger

logger = get_logger(__name__)

router = APIRouter()
book = book_db.BookDB()

@router.post("/")
def create_book(data: books.Book):
    try:
        book.create_book(data.__dict__)
        raise HTTPException(status_code=201, detail="Book created successfully")
    except KeyError:
        raise HTTPException(status_code=422, detail="genre is unique")

@router.get("/")
def get_all_books():
    return book.get_all_books()

@router.put("/{id}")
def update_books(id: int, body: books.Book):
    try:
        return book.update_book(id, body)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"{e}")

@router.get("/{id}")
def book_by_id(id: int):
    try:
        return book.get_book_by_id(id)
    except KeyError:
        logger.error("id not found")
        raise HTTPException(status_code=404, detail="id not found")
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail=f"{e}")

@router.put("/{id}/return/{member_id}")
def set_available(id, val, member_id):
    pass

@router.put("/{id}/borrow/{member_id}")
def set_available(id, val, member_id):
    pass

@router.get("/{member_id}")
def count_borrows_by_member(member_id: int):
    return book.count_active_borrows_by_member(member_id)

@router.put("/{id}/borrow/{member_id}")
def count_active_borrows_by_member(member_id):
    pass