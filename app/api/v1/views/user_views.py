from flask import jsonify, request
from ...v1 import version_1 as v1
from ..schemas.user_schema import UserSchema
from ..models.user_model import User

db = User()

@v1.route('/', methods=['GET'])
@v1.route('/welcome', methods=['GET'])
def index():
    return jsonify({'status': 200, 'message': 'Welcome !! A meetup Application:'}), 200

@v1.route('/register', methods=['POST'])
def register():
    """ Function to register new user """
    json_data = request.get_json()

    # No data has been provided
    if not json_data:
        return jsonify({'status': 400, 'message': 'No Sign up data provided'}), 400

    # Check if request is valid
    data, errors = UserSchema().load(json_data)
    if errors:
        return jsonify({'status': 400, 'message' : 'Invalid data. Please fill all the required fields', 'errors': errors}), 400


    # Checking  if  the username exists
    if db.exists('username', data['username']):
        return jsonify({'status': 409, 'message' : 'Username already exists'}), 409

    # Checking  if the  email exists
    if db.exists('email', data['email']):
        return jsonify({'status': 409, 'message' : 'Email already exists'}), 409

    # Save new user and get result
    new_user = db.save(data)
    result = UserSchema(exclude=['password']).dump(new_user).data

    
    return jsonify({
        'status': 201, 
        'message' : 'User created successfully', 
        'data': result, 
       
        }), 201
