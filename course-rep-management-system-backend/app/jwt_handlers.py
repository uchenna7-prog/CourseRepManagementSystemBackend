from flask import jsonify
from app.extensions import jwt

def register_jwt_handlers():
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({"msg": "Token has expired"}), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(err_msg):
        return jsonify({"msg": "Invalid token"}), 422

    @jwt.unauthorized_loader
    def missing_token_callback(err_msg):
        return jsonify({"msg": "Missing token"}), 401
