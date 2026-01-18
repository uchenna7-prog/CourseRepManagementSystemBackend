from app.database.repositories.course_mate_repo import CourseMateRepository

class CourseMateService:

    @staticmethod
    def get_all_course_mates(course_rep_id):
        return CourseMateRepository.find_all(course_rep_id)

    @staticmethod
    def get_course_mate(course_rep_id, course_mate_id):
        return CourseMateRepository.find_one(course_rep_id ,course_mate_id)

    @staticmethod
    def search_course_mates(course_rep_id, search_query):
        return CourseMateRepository.search(course_rep_id,  search_query)

    @staticmethod
    def add_course_mate(course_rep_id, first_name, middle_name, last_name, email, mat_number):
        return CourseMateRepository.add(course_rep_id,first_name, middle_name, last_name, email, mat_number)

    @staticmethod
    def delete_course_mate(course_rep_id, course_mate_id):
        CourseMateRepository.delete(course_rep_id, course_mate_id)
