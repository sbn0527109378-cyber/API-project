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
    
    @staticmethod
    def get_member_by_id(id: int):
        logger.debug("User wants to see a member by id")
        conn = db_connection.connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM members WHERE id = %s;"
        value = id,
        cursor.execute(sql, value)
        member = cursor.fetchone()
        cursor.close()
        conn.close()
        logger.info("The member were successfully displayed")
        if member:
            return member
        raise KeyError
    
    @staticmethod
    def update_bmember(id, body):
        logger.debug("User wants to update a member")
        conn = db_connection.connection()
        cursor = conn.cursor(dictionary=True)
        sql = "UPDATE members SET name = %s, email = %s WHERE id = %s;"
        values = body.name, body.email, id
        logger.warning("User updating a member to mysql")
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("The member was updated successfully")
        return "The member was updated successfully"
    
    @staticmethod
    def deactivate_member(id):
        logger.debug("User wants to update is_active=False")
        conn = db_connection.connection()
        cursor = conn.cursor(dictionary=True)
        sql = "UPDATE members SET is_active = FALSE WHERE id = %s;"
        values = id,
        logger.warning("User updating is_active=False to mysql")
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("The member was updated successfully")
        return "The member was updated successfully"
    
    @staticmethod
    def activate_member(id):
        logger.debug("User wants to update is_active=True")
        conn = db_connection.connection()
        cursor = conn.cursor(dictionary=True)
        sql = "UPDATE members SET is_active = TRUE WHERE id = %s;"
        values = id,
        logger.warning("User updating is_active=True to mysql")
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("The member was updated successfully")
        return "The member was updated successfully"
    
    @staticmethod
    def increment_borrows(id):
        logger.debug("increase the borrow by 1")
        conn = db_connection.connection()
        cursor = conn.cursor()
        sql = "SELECT total_borroes FROM members WHERE id = %s;"
        values = id,
        cursor.execute(sql, values)
        borrow = cursor.fetchone()
        sql1 = "UPDATE members SET total_borroes = %s WHERE id = %s;"
        values1 = (borrow[0] + 1), id
        logger.warning("User updating increase the borrow by 1 to mysql")
        cursor.execute(sql1, values1)
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("The borrow was updated successfully")
        return "The borrow was updated successfully"
    
    @staticmethod
    def get_top_member():
        logger.debug("get top member")
        conn = db_connection.connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT id, total_borroes FROM members;"
        cursor.execute(sql)
        all_total_borroes = cursor.fetchall()
        cursor.close()
        conn.close()
        maxi = None
        id = None
        for borrow in all_total_borroes:
            if maxi is None or borrow["total_borroes"] > maxi:
                maxi = borrow["total_borroes"]
                id = borrow["id"]
        logger.info("returns count books member id")
        if not maxi == 0:
            return {"id": id, "total_borroes":maxi}
        raise KeyError