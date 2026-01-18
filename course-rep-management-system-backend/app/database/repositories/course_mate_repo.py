from . import get_db

class CourseMateRepository:

    @staticmethod
    def find_all(course_rep_id):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT courseMateId, firstName, middleName, lastName, email, matNumber
            FROM coursemates
            WHERE courseRepId = %s
            ORDER BY firstName, lastName
        """
        cursor.execute(query, (course_rep_id,))
        result = cursor.fetchall()
        cursor.close()
        return result

    @staticmethod
    def find_one(course_rep_id,course_mate_id):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT courseMateId, firstName, middleName, lastName, email, matNumber
            FROM coursemates
            WHERE courseRepId = %s AND courseMateId = %s
        """
        cursor.execute(query, (course_rep_id,course_mate_id))
        result = cursor.fetchone()
        cursor.close()
        return result

    @staticmethod
    def search(course_rep_id,search_query):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        pattern = f"%{search_query.lower()}%"
        query = """
            SELECT courseMateId, firstName, middleName, lastName, email, matNumber
            FROM coursemates
            WHERE courseRepId = %s
            AND (
                LOWER(firstName) LIKE %s
                OR LOWER(middleName) LIKE %s
                OR LOWER(lastName) LIKE %s
                OR LOWER(matNumber) LIKE %s
            )
            ORDER BY firstName, lastName
        """
        cursor.execute(query, (course_rep_id, pattern, pattern, pattern, pattern))
        result = cursor.fetchall()
        cursor.close()
        return result

    @staticmethod
    def add(course_rep_id,first_name, middle_name, last_name, email, mat_number):
        db = get_db()
        cursor = db.cursor()
        query = """
            INSERT INTO coursemates (courseRepId, firstName, middleName, lastName, email, matNumber)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (course_rep_id,first_name, middle_name, last_name, email, mat_number))
        db.commit()
        new_id = cursor.lastrowid
        cursor.close()
        return {
            "courseMateId": new_id,
            "firstName": first_name,
            "middleName": middle_name,
            "lastName":  last_name,
            "email": email,
            "matNumber": mat_number
        }

    @staticmethod
    def delete(course_rep_id, course_mate_id):
        db = get_db()
        cursor = db.cursor()
        query = """
            DELETE FROM coursemates
            WHERE courseRepId = %s AND courseMateId = %s
        """
        cursor.execute(query, (course_rep_id, course_mate_id))
        db.commit()
        cursor.close()
