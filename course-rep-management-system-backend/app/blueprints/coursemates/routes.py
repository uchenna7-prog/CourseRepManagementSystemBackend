from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from . import course_mates_bp
from app.blueprints.coursemates.services import CourseMateService


@course_mates_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_course_mates():
    claims = get_jwt()
    course_rep_id = claims['courseRepId']
    course_mates = CourseMateService.get_all_course_mates(course_rep_id)
    return jsonify(courseMates=course_mates), 200


@course_mates_bp.route('/search', methods=['GET'])
@jwt_required()
def search_course_mates():
    claims = get_jwt()
    course_rep_id = claims['courseRepId']
    query = request.args.get('q', '').strip()
    course_mates = CourseMateService.search_course_mates(course_rep_id, query)
    return jsonify(courseMates=course_mates), 200


@course_mates_bp.route('/<int:courseMateId>', methods=['GET'])
@jwt_required()
def get_course_mate(course_mate_id):
    claims = get_jwt()
    course_rep_id = claims['courseRepId']
    course_mate = CourseMateService.get_course_mate(course_rep_id,course_mate_id)
    if not course_mate :
        return jsonify({'message': 'Course mate not found'}), 404
    return jsonify(courseMate=course_mate ), 200


@course_mates_bp.route('/', methods=['POST'])
@jwt_required()
def add_course_mate():
    claims = get_jwt()
    course_rep_id = claims['courseRepId']
    data = request.get_json()
    required_fields = ['firstName', 'lastName', 'email', 'matNumber']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing required field'}), 400

    new_course_mate = CourseMateService.add_course_mate(
        course_rep_id,
        firstName=data['firstName'],
        middleName=data.get('middleName'),
        lastName=data['lastName'],
        email=data['email'],
        matNumber=data['matNumber']
    )
    return jsonify({'message': 'Course mate added', 'courseMate': new_course_mate}), 201


@course_mates_bp.route('/<int:courseMateId>', methods=['DELETE'])
@jwt_required()
def delete_course_mate(course_mate_id):
    claims = get_jwt()
    course_rep_id = claims['courseRepId']
    CourseMateService.delete_course_mate(course_rep_id, course_mate_id)
    return jsonify({'message': 'Course mate deleted'}), 200
