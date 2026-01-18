from flask import request, jsonify, make_response
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity, get_jwt
)
from . import auth_bp
from app.blueprints.auth.services import AuthService


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    required_fields = ['firstName', 'lastName', 'email', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing required field'}), 400

    user_id, error = AuthService.register_user(
        first_name=data['firstName'],
        middle_name=data.get('middleName'),
        last_name=data['lastName'],
        email=data['email'],
        password=data['password']
    )

    if error:
        return jsonify({'message': error}), 400

    return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 201



@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    required_fields = ['email', 'password']

    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Email and password required'}), 400

    user, error = AuthService.login_user(
        email=data['email'],
        password=data['password']
    )

    if error:
        return jsonify({'message': error}), 401

    identity = user['email']
    additional_claims = {
        "courseRepId": user['courseRepId'],
        "firstName": user['firstName'],
        "middleName": user.get('middleName'),
        "lastName": user['lastName']
    }

    access_token = create_access_token(
        identity=identity,
        additional_claims=additional_claims
    )

    refresh_token = create_refresh_token(identity=identity)

    response = make_response(jsonify({
        'message': 'Login successful',
        'user': {
            'id': user['courseRepId'],
            'firstName': user['firstName'],
            'middleName': user.get('middleName'),
            'lastName': user['lastName'],
            'email': user['email']
        },
        'accessToken': access_token
    }))

    response.set_cookie(
        'refreshToken',
        refresh_token,
        httponly=True,
        secure=False,
        samesite='Strict',
        path='/auth/refresh'
    )
    return response, 200


@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_email = get_jwt_identity()
    claims = get_jwt()
    return jsonify(
        msg=f"Hello, {claims['firstName']}!",
        email=current_user_email,
        role=claims['role']
    )


@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user_email = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user_email)
    return jsonify(accessToken=new_access_token)
@auth_bp.route('/logout', methods=['POST'])
def logout():
    response = jsonify({'message': 'Logged out'})
    response.set_cookie(
        'refreshToken',
        '',
        httponly=True,
        expires=0,
        path='/auth/refresh'
    )
    return response



