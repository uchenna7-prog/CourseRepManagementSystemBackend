from flask import Blueprint

activity_record_bp = Blueprint('activity_record', __name__)

from . import routes