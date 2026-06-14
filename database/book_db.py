from database import db_connection
from pydantic_classes import books
from logs.logger_config import get_logger

logger = get_logger(__name__)


class BookDB:
    @staticmethod
    def create_book(data: books.Book):
        logger.debug("User wants to create a new book")
        conn = db_connection.connection()
        cursor = conn.cursor(dictionary=True)
        sql = "INSERT INTO books (title, author, genre) VALUES (%s, %s, %s);"
        values = data["title"], data["author"], data["genre"]
        logger.warning("User adds a new book to mysql")
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("The new book was added successfully")
        return "The new book was added successfully"

    @staticmethod
    def get_all_books():
        logger.debug("User wants to see all books")
        conn = db_connection.connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM books;"
        cursor.execute(sql)
        all_books = cursor.fetchall()
        cursor.close()
        conn.close()
        logger.info("The books were successfully displayed")
        if all_books:
            return all_books
        return {}
    
    @staticmethod
    def get_book_by_id(id: int):
        logger.debug("User wants to see a book by id")
        conn = db_connection.connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM books WHERE id = %s;"
        value = id,
        cursor.execute(sql, value)
        book = cursor.fetchone()
        cursor.close()
        conn.close()
        logger.info("The book were successfully displayed")
        if book:
            return book
        raise KeyError
    
    @staticmethod
    def update_book(id, body):
        logger.debug("User wants to update a book")
        conn = db_connection.connection()
        cursor = conn.cursor(dictionary=True)
        sql = "UPDATE books SET title = %s, author = %s, genre = %s WHERE id = %s;"
        values = body.title, body.author, body.genre, id
        logger.warning("User updating a book to mysql")
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("The book was updated successfully")
        return "The book was updated successfully"
    

    
    

