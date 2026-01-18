from . import get_db

class ActivityRecordRepository:

    @staticmethod
    def find_all(activity_id):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT courseMateId, activityId, statusTypeId
            FROM courseMateActivityRecords
            WHERE activityId = %s
            ORDER BY date_created DESC
        """
        cursor.execute(query, (activity_id,))
        result = cursor.fetchall()
        cursor.close()
        return result

    @staticmethod
    def find_one(activity_id, course_mate_id):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT courseMateId, activityId, statusTypeId
            FROM courseMateActivityRecords
            WHERE  activityId = %s AND courseMateId= %s
        """
        cursor.execute(query, (activity_id, course_mate_id))
        result = cursor.fetchone()
        cursor.close()
        return result

    @staticmethod
    def create(course_mate_id, activity_id, status_type_id):
        db = get_db()
        cursor = db.cursor()
        query = """
            INSERT INTO courseMateActivityRecords (courseMateId, activityId, statusTypeId)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (course_mate_id, activity_id, status_type_id))
        db.commit()
        new_id = cursor.lastrowid
        cursor.close()
        return new_id

    @staticmethod
    def delete(activity_id, course_mate_id):
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM courseMateActivityRecords WHERE activityId = %s AND courseMateId= %s"
        cursor.execute(query, (activity_id, course_mate_id))
        db.commit()
        cursor.close()
