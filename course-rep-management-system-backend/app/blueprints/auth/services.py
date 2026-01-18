from flask_bcrypt import generate_password_hash,check_password_hash
from app.database.repositories.course_rep_repo import CourseRepRepository

class AuthService:

    @staticmethod
    def register_user(first_name, middle_name, last_name, email, password):
        existing_user = CourseRepRepository.find_by_email(email)
        if existing_user:
            return None, "Email already registered"
        password_hash = generate_password_hash(password).decode("utf-8")
        user_id = CourseRepRepository.create(first_name, middle_name, last_name, email, password_hash)
        return user_id, None

    @staticmethod
    def login_user(email, password):
        user = CourseRepRepository.find_by_email(email)
        if not user:
            return None, "Invalid credentials"
        if check_password_hash(user['passwordHash'], password):
            return user, None
        return None, "Invalid credentials"
