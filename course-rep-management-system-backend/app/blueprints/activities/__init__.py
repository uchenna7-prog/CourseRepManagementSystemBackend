from flask import Blueprint

activities_bp = Blueprint('activities', __name__)

from . import routes