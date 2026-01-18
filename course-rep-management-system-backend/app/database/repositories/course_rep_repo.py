from . import get_db

class CourseRepRepository:

    @staticmethod
    def find_by_email(email):
        db = get_db()
        cursor = db.cursor(dictionary=True)

        query = """
            SELECT courseRepId, firstName, middleName, lastName, email, passwordHash
            FROM courseReps
            WHERE email = %s
        """
        cursor.execute(query, (email,))
        return cursor.fetchone()

    @staticmethod
    def create(first_name, middle_name, last_name, email, password_hash):
        db = get_db()
        cursor = db.cursor()
        query = """
            INSERT INTO courseReps (firstName, middleName, lastName, email, passwordHash)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (first_name, middle_name, last_name, email, password_hash))
        db.commit()
        return cursor.lastrowid
