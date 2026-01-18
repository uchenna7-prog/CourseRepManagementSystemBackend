from app.database.repositories.activity_repo import ActivityRepository

class ActivityService:

    @staticmethod
    def get_all_activities(course_rep_id):
        return ActivityRepository.find_all(course_rep_id)

    @staticmethod
    def get_activity(course_rep_id,activity_name):
        return ActivityRepository.find_one(course_rep_id,activity_name)

    @staticmethod
    def create_activity(course_rep_id, activity_name, activity_type_id, description):
        return ActivityRepository.create(course_rep_id,activity_name,activity_type_id, description)

    @staticmethod
    def delete_activity(course_rep_id,activity_name):
        ActivityRepository.delete(course_rep_id,activity_name)
