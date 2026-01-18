from flask import Flask, jsonify
from app.config import Config
from app.extensions import bcrypt, jwt, cors
from app.database.connection import close_db
from app.jwt_handlers import register_jwt_handlers

from app.blueprints.auth import auth_bp
from app.blueprints.coursemates import course_mates_bp
from app.blueprints.activities import activities_bp
from app.blueprints.activity_record import activity_record_bp

from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]

    CORS(
        app,
        supports_credentials=True,
        origins=["http://localhost:5173"]
    )

    bcrypt.init_app(app)
    jwt.init_app(app)

    app.teardown_appcontext(close_db)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(course_mates_bp, url_prefix='/coursemates')
    app.register_blueprint(activities_bp, url_prefix='/activities')
    app.register_blueprint(activity_record_bp, url_prefix='/activity_record')

    @app.route('/health', methods=['GET'])
    def health_check():
        return {'status': 'healthy'}, 200

    register_jwt_handlers()

    return app
