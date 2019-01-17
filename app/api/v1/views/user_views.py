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


@v1.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()

    # Check if the request contains any data
    if not json_data:
        return jsonify({'status': 400, 'message': 'No data has provided! Please put your login credentials'}), 400

    # Check if credentials have been passed
    data, errors = UserSchema().load(json_data, partial=True)
    if errors:
        return jsonify({'status': 400, 'message': 'Invalid data. Please fill all required fields', 'errors': errors}), 400

    try:
        username = data['username']
        password = data['password']
    except:
        return jsonify({'status': 400, 'message': 'Invalid credentials.Confirm!'}), 400

    # Check if username exists
    if not db.exists('username', username):
        return jsonify({'status': 404, 'message' : 'User not found'}), 404

    user = db.find_by_username(username)

    # Checking if password match
    db.checkpassword(user['password'], password)

   
    return jsonify({
        'status': 200, 
        'message': 'User logged in successfully',
       
        }), 200


    