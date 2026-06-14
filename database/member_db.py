from database import db_connection
from logs.logger_config import get_logger

logger = get_logger(__name__)



class MemberDB:
    @staticmethod
    def create_member(data):
        logger.debug("User wants to create a new member")
        conn = db_connection.connection()
        cursor = conn.cursor()
        sql = "INSERT INTO members (name, email) VALUES (%s, %s);"
        values = data.name, data.email
        logger.warning("creating a member")
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("new member created successfully")
        return "new member created successfully"
    
    @staticmethod
    def get_all_members():
        logger.debug("all members")
        conn = db_connection.connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM members;"
        cursor.execute(sql)
        all_members = cursor.fetchall()
        cursor.close()
        conn.close()
        logger.info("returns all members")
        return all_members