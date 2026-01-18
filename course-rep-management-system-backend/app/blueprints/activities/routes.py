from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from . import activities_bp
from app.blueprints.activities.services import ActivityService


@activities_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_activities():
    claims = get_jwt()
    course_rep_id = claims['courseRepId']
    activities = ActivityService.get_all_activities(course_rep_id)
    return jsonify(activities=activities), 200


@activities_bp.route('/<string:activity_name>', methods=['GET'])
@jwt_required()
def get_one_activity(activity_name):
    claims = get_jwt()
    course_rep_id = claims['courseRepId']
    activity = ActivityService.get_activity(course_rep_id,activity_name)
    if not activity:
        return jsonify({'message': 'Activity not found'}), 404
    return jsonify(activity=activity), 200


@activities_bp.route('/', methods=['POST'])
@jwt_required()
def create_activity():
    data = request.get_json()
    required_fields = ['courseRepId', 'activityName', 'description']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing required field'}), 400

    new_id = ActivityService.create_activity(
        course_rep_id=data['courseRepId'],
        activity_name=data['activityName'],
        description=data['description']
    )
    return jsonify({'message': 'Activity created', 'activityId': new_id}), 201


@activities_bp.route('/<string:activity_name>', methods=['DELETE'])
@jwt_required()
def delete_activity(activity_id):
    claims = get_jwt()
    course_rep_id = claims['courseRepId']
    ActivityService.delete_activity(course_rep_id,activity_name)
    return jsonify({'message': 'Activity deleted'}), 200
