import mysql.connector


def connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="library_db"
    )


def create_tables_books_and_members():
    conn = connection()
    cursor = conn.cursor()
    sql1 = """CREATE TABLE IF NOT EXISTS books(
    id                      INT                     AUTO_INCREMENT PRIMARY KEY,
    title                   VARCHAR(50)             NOT NULL,
    author                  VARCHAR(50)             NOT NULL,
    genre                   ENUM(Fiction,
    Non-Fiction, Science, History, Other)           NOT NULL,
    is_available            BOOLEAN DEFAULT TRUE    NOT NULL,
    borrowed_by_member_id   INT DEFAULT NULL"""

    sql2 = """CREATE TABLE IF NOT EXISTS members(
    id                  INT                     AUTO_INCREMENT PRIMARY KEY,
    name                VARCHAR(50)             NOT NULL,
    email               VARCHAR(50)             UNIQUE NOT NULL,
    is_active           BOOLEAN DEFAULT TRUE    NOT NULL
    total_borroes       INT DEFAULT 0"""

    cursor.execute(sql1)
    cursor.execute(sql1)

    conn.commit()

    cursor.close()
    conn.close()
    