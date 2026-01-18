from app.database.repositories.activity_record_repo import ActivityRecordRepository

class ActivityRecordService:

    @staticmethod
    def get_all_records(course_rep_id):
        return ActivityRecordRepository.find_all_by_course_rep(course_rep_id)

    @staticmethod
    def get_record(course_rep_id, record_id):
        return ActivityRecordRepository.find_by_id(course_rep_id, record_id)

    @staticmethod
    def create_record(course_rep_id, activity_id, title, description):
        return ActivityRecordRepository.create(course_rep_id, activity_id, title, description)

    @staticmethod
    def delete_record(course_rep_id, record_id):
        ActivityRecordRepository.delete(course_rep_id, record_id)
