from . import get_db

class ActivityRepository:

    @staticmethod
    def find_all(course_rep_id):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT courseRepId, activityName, description, createdAt
            FROM activities
            WHERE courseRepId = %s
            ORDER BY date_created DESC
        """
        cursor.execute(query,(course_rep_id,))
        return cursor.fetchall()

    @staticmethod
    def find_one(course_rep_id,activity_name):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT courseRepId, activityName, description,createdAt
            FROM activities
            WHERE courseRepId = %s AND activityName = %s
        """
        cursor.execute(query, (course_rep_id,activity_name))
        return cursor.fetchone()

    @staticmethod
    def create(course_rep_id, activity_name,activity_type_id, description):
        db = get_db()
        cursor = db.cursor()
        query = """
            INSERT INTO activities (courseRepId, activityName, description)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (course_rep_id, activity_name, activity_type_id, description))
        return cursor.lastrowid

    @staticmethod
    def delete(course_rep_id,activity_name):
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM activities WHERE courseRepId = %s AND activityName = %s"
        cursor.execute(query, (course_rep_id,activity_name))
