from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from . import activity_record_bp
from app.blueprints.activity_record.services import ActivityRecordService

# ---------------------------
# Get all activity records for logged-in course rep
# ---------------------------
@activity_record_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_records():
    claims = get_jwt()
    course_rep_id = claims['courseRepId']

    records = ActivityRecordService.get_all_records(course_rep_id)
    return jsonify(records=records), 200

# ---------------------------
# Get a single record by ID
# ---------------------------
@activity_record_bp.route('/<int:record_id>', methods=['GET'])
@jwt_required()
def get_record(record_id):
    claims = get_jwt()
    course_rep_id = claims['courseRepId']

    record = ActivityRecordService.get_record(course_rep_id, record_id)
    if not record:
        return jsonify({'message': 'Record not found'}), 404
    return jsonify(record=record), 200

# ---------------------------
# Create a new activity record
# ---------------------------
@activity_record_bp.route('/', methods=['POST'])
@jwt_required()
def create_record():
    claims = get_jwt()
    course_rep_id = claims['courseRepId']

    data = request.get_json()
    required_fields = ['activityId', 'title', 'description']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing required field'}), 400

    new_id = ActivityRecordService.create_record(
        course_rep_id,
        activity_id=data['activityId'],
        title=data['title'],
        description=data['description']
    )
    return jsonify({'message': 'Activity record created', 'recordId': new_id}), 201

# ---------------------------
# Delete an activity record
# ---------------------------
@activity_record_bp.route('/<int:record_id>', methods=['DELETE'])
@jwt_required()
def delete_record(record_id):
    claims = get_jwt()
    course_rep_id = claims['courseRepId']

    ActivityRecordService.delete_record(course_rep_id, record_id)
    return jsonify({'message': 'Activity record deleted'}), 200
