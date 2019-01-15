from flask import jsonify, request
from ...v1 import version_1 as v1
from ..schemas.meetup_schema import MeetupSchema
from ..models.meetup_model import Meetup


db = Meetup()


@v1.route('/meetups', methods=['POST'])
def create_meetup():
    """ create meetup function """
    json_data = request.get_json()

    # when no data is provided
    if not json_data:
        return jsonify({'status': 400, 'error': 'No data provided'}), 400

    # whether the request is valid
    data, errors = MeetupSchema().load(json_data)
    if errors:
        return jsonify({'status': 400, 'error' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400

    # Save new meetup when request is verified
    new_meetup = db.save(data)
    result = MeetupSchema().dump(new_meetup).data
    return jsonify({'status': 201, 'message': 'Meetup created successfully', 'data': [result]}), 201



@v1.route('/meetups/<int:meetup_id>', methods=['GET'])
def fetch_meetup(meetup_id):

    """  fetch specific meetup function """
    # Check if meetup exists 
    if not db.exists('id', meetup_id):
        return  jsonify({'status': 404, 'error': 'Meetup not found'}), 404

    # Get meetups 
    meetups = db.fetch_by_id(meetup_id)
    result = MeetupSchema(many=True).dump(meetups).data
    return jsonify({'status':200, 'data':result}), 200


@v1.route('/meetups/upcoming', methods=['GET'])
def fetch_upcoming_meetups():
    """  fetch all meetups fuction """
    meetups = db.all()
    result = MeetupSchema(many=True).dump(meetups).data
    return jsonify({'status':200, 'data':result}), 200

    