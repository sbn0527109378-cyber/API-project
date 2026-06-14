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

@router.get("/")
def get_all_books():
    return book.get_all_books()

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
    
@router.put("/{id}")
def update_books(id: int, body: books.Book):
    return book.update_book(id, body)