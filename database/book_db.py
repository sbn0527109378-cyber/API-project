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
        if data["genre"] not in ["Fiction", "Non-Fiction", "Science", "History", "Other"]:
            raise KeyError
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
        sql = "SELECT id FROM books;"
        cursor.execute(sql)
        all_ids = cursor.fetchall()
        is_exsist = [True for id1 in all_ids if id1["id"] == id]

        if is_exsist:
            sql = "UPDATE books SET title = %s, author = %s, genre = %s WHERE id = %s;"
            values = body.title, body.author, body.genre, id
            logger.warning("User updating a book to mysql")
            cursor.execute(sql, values)
            conn.commit()
            logger.info("The book was updated successfully")
            cursor.close()
            conn.close()
            return "The book was updated successfully"
        cursor.close()
        conn.close()
        raise KeyError


    # def set_available(id, val, member_id):
    #     logger.debug("User wants to update availability")
    #     conn = db_connection.connection()
    #     cursor = conn.cursor(dictionary=True)
    #     sql = "UPDATE books SET title = %s, author = %s, genre = %s WHERE id = %s;"
    #     values = body.title, body.author, body.genre, id
    #     logger.warning("User updating a book to mysql")
    #     cursor.execute(sql, values)
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #     logger.info("The book was updated successfully")
    #     return "The book was updated successfully"

    @staticmethod
    def count_total_books():
        logger.debug("count books")
        conn = db_connection.connection()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM books;"
        cursor.execute(sql)
        count_all_books = cursor.fetchone()
        cursor.close()
        conn.close()
        logger.info("returns count books")
        return count_all_books

    @staticmethod
    def count_available_books():
        logger.debug("count available books")
        conn = db_connection.connection()
        cursor = conn.cursor()
        sql = "SELECT SUM(is_available = 1) FROM books;"
        cursor.execute(sql)
        count_available_books = cursor.fetchone()
        cursor.close()
        conn.close()
        logger.info("returns count available books")
        return count_available_books
    
    @staticmethod
    def count_borrowed_books():
        logger.debug("count borrowed books")
        conn = db_connection.connection()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM books WHERE is_available = 0;"
        cursor.execute(sql)
        count_borrowed_books = cursor.fetchone()
        cursor.close()
        conn.close()
        logger.info("returns count borrowed books")
        return count_borrowed_books
    
    @staticmethod
    def count_books_by_genre(genre):
        logger.debug("count books by genre")
        conn = db_connection.connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT COUNT(*) FROM books WHERE genre = %s;"
        value = genre,
        cursor.execute(sql, value)
        count_books_by_genre = cursor.fetchall()
        cursor.close()
        conn.close()
        logger.info("returns count books by genre")
        return count_books_by_genre
    
    @staticmethod
    def count_active_borrows_by_member(member_id):
        logger.debug("count books by member id")
        conn = db_connection.connection()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM books WHERE borrowed_by_member_id = %s;"
        value = member_id,
        cursor.execute(sql, value)
        count_books_by_genre = cursor.fetchone()
        cursor.close()
        conn.close()
        logger.info("returns count books member id")
        return count_books_by_genre
    
    @staticmethod
    def count_active_members():
        logger.debug("count active members")
        conn = db_connection.connection()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM members WHERE is_active = TRUE;"
        cursor.execute(sql)
        count_books_by_genre = cursor.fetchone()
        cursor.close()
        conn.close()
        logger.info("returns count books member id")
        return count_books_by_genre