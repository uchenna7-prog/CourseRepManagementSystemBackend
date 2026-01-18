from flask import Blueprint

course_mates_bp = Blueprint('course_mates', __name__)

from . import routes
