from database import db_connection
from pydantic_classes import books


class BookDB:
    @staticmethod
    def create_book(data: books.Book):
        conn = db_connection.connection()
        cursor = conn.cursor()
        sql = "INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)"
        values = data["title"], data["author"], data["genre"]
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()