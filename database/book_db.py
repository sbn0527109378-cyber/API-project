from database import db_connection
from pydantic_classes import books
from logs.logger_config import get_logger

logger = get_logger(__name__)


class BookDB:
    @staticmethod
    def create_book(data: books.Book):
        logger.debug("User wants to create a new book")
        conn = db_connection.connection()
        cursor = conn.cursor()
        sql = "INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)"
        values = data["title"], data["author"], data["genre"]
        logger.warning("User adds a new book to mysql")
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("The new book was added successfully")