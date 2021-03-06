import unittest
from flask import json
from app import create_app
from app.api.v1.models.user_model import users


class TestMeetups(unittest.TestCase):
    

    def setUp(self):

        """ Initialize app instance and testclient """
        self.app = create_app('testing')
        self.client = self.app.test_client()
       
    
    def tearDown(self):
        """runs after every testcase"""

        self.app = None
        users.clear()


    def test_signup_when_no_data_provied(self):
        """ Test sign up with no data sent """
        response = self.client.post('/api/v1/register')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'No Sign up data provided')
    
    def test_signup_when_empty_data_provided(self):
        """ Test sign up with empty data sent """
        user = {}

        response = self.client.post('/api/v1/register', json=json.dumps(user), headers={'Content-Type': 'application/json'})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all the required fields')

    def test_signup_when_there_are_missing_fields(self):
        """ Test signup with missing fields in data sent """
        user = {
            'firstname' : 'Caleb',
            'lastname' : 'Mbugua',
            'password' : '12345566'
        }

        response = self.client.post('/api/v1/register', json=user, headers={'Content-Type': 'application/json'})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all the required fields')
    
    def test_signup_invalid_password_provided(self):
        """ Test signup with invalid password """

        user = {
            'firstname' : 'Caleb',
            'lastname' : 'Mbugua',
            'username' : 'MbuguaCaleb',
            'email' : 'mbuguacaleb30@gmail.com',
            'password' : '123456',
            'phone_number' : '0704699193'
        }

        response = self.client.post('/api/v1/register', json=user, headers={'Content-Type': 'application/json'})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all the required fields')

    def test_signup_invalid_email(self):
        """ Test sign up with invalid email """
        
        user = {
            'firstname' : 'Caleb',
            'lastname' : 'Mbugua',
            'username' : 'MbuguaCaleb',
            'email' : 'mbuguac',
            'password' : '123456',
            'phone_number' : '0704699193'
        }

       
        response = self.client.post('/api/v1/register', json=user, headers={'Content-Type': 'application/json'})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all the required fields')
    
    def test_signup(self):
        """ Test sign up with correct data """
        
        user = {
            'firstname' : 'Caleb',
            'lastname' : 'Mbugua',
            'username' : 'MbuguaCaleb',
            'email' : 'mbuguacaleb30@gmail.com',
            'password' : 'Calebmbugua1#',
            'phone_number' : '0704699193'
        }
        

        response = self.client.post('/api/v1/register', json=user, headers={'Content-Type': 'application/json'})
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'User created successfully')
        self.assertEqual(data['data']['username'], user['username'])


    def test_user_login_when_no_data_provided(self):

        """ Test login with no data has been provided """

        response= self.client.post('/api/v1/login')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'No data has provided! Please put your login credentials')

   
    def test_login_for_unregistered_user(self):
        """ Test login with an un unregistered user credentials """
        user = {
            'username' : 'Gabriel',
            'password' : '##@qssR7qq'
        }

        response = self.client.post('/api/v1/login', json=user, headers={'Content-Type': 'application/json'})
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'User not found')

    def test_login_success(self):
        """ Test successfull login """
        # Register user

        
        user = {
            "firstname":"caleb",
	        "lastname":"mbugua",
	        "username":"MbuguaCaleb",
	        "email":"mbuguacaleb30@gmail.com",
	        "password":"Mbuguacaleb1#",
	        "phone_number":"0704699193"
	
        }


        res_1 = self.client.post('/api/v1/register', json=user, headers={'Content-Type': 'application/json'})
        data_1 = res_1.get_json()

        self.assertEqual(res_1.status_code, 201)
        self.assertEqual(data_1['status'], 201)

        # Login user
        res_2 = self.client.post('/api/v1/login', json={'username': 'MbuguaCaleb', 'password': 'Mbuguacaleb1#'}, headers={'Content-Type': 'application/json'})
        data_2 = res_2.get_json()

        self.assertEqual(res_2.status_code, 200)
        self.assertEqual(data_2['status'], 200)
        self.assertEqual(data_2['message'], 'User logged in successfully')

    def test_login_when_no_username_provided(self):
        """ Test login with no username provided """
        # Register user


        
        user = {
            "firstname":"caleb",
	        "lastname":"mbugua",
	        "username":"MbuguaCaleb",
	        "email":"mbuguacaleb30@gmail.com",
	        "password":"Mbuguacaleb1#",
	        "phone_number":"0704699193"
	
        }

        res_1 = self.client.post('/api/v1/register', json=user, headers={'Content-Type': 'application/json'})
        data_1 = res_1.get_json()

        self.assertEqual(res_1.status_code, 201)
        self.assertEqual(data_1['status'], 201)

        # Login user
        res_2 = self.client.post('/api/v1/login', json={'password': 'Mbuguacaleb1#'}, headers={'Content-Type': 'application/json'})
        data_2 = res_2.get_json()

        self.assertEqual(res_2.status_code, 400)
        self.assertEqual(data_2['status'], 400)
        self.assertEqual(data_2['message'], 'Invalid credentials.Confirm!')

  