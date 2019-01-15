import unittest
from flask import json
from app import create_app
from app.api.v1.models.meetup_model import meetups


class TestMeetups(unittest.TestCase):
    

    def setUp(self):

        """ Initialize app instance and testclient """
        self.app = create_app('testing')
        self.client = self.app.test_client()
       
    
    def tearDown(self):
        """runs after every testcase"""

        self.app = None
        meetups.clear()
       

    """Test cases """

    def test_create_meetup_no_data(self):

        """ Testing while there is no data sent when creating meetup """
        response = self.client.post('/api/v1/meetups')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'No data provided')


    def test_create_meetup_empty_data(self):

        """ Test while there is no data sent """
        meetup = {}

        response = self.client.post('/api/v1/meetups', json=json.dumps(meetup), content_type="application/json")
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'Invalid data. Please fill all required fields')


    def test_create_meetup_missing_fields(self):

        """ Test create meetup with missing fields in request """

        # Create meetup without location
        meetup = {

            'topic' : 'Machine learning',
            'happening_on' : '18/01/2019',
            
        }

        response = self.client.post('/api/v1/meetups', json=meetup, content_type="application/json")
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'Invalid data. Please fill all required fields')

    def test_create_meetup(self):

        """ Test create meetup """

        meetup = {

            'topic' : 'Datascience',
            'location' : 'Naivasha',
            'happening_on' : '17/01/2019'
           
        }

        res = self.client.post('/api/v1/meetups', json=meetup, content_type="application/json")
        data = res.get_json()
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'Meetup created successfully')


    def test_fetch_specific_meetup(self):
        """ Test fetch a specific meetup using id """
        # Create meetups
        meetup = {

            'topic' : 'Datascience',
            'location' : 'Nairobi',
            'happening_on' : '17/01/2019'
            
            
        }

        meetup2 = {
            'topic' : 'AI',
            'location' : 'Andela',
            'happening_on' : '18/01/2019',
            
        }
        self.client.post('/api/v1/meetups', json=meetup, content_type="application/json")
        self.client.post('/api/v1/meetups', json=meetup2, content_type="application/json")

        res = self.client.get('/api/v1/meetups/1')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['data'][0]['id'], 1)

    def test_fetch_non_existent_meetup(self):

        """ Test for  a existent meetup """
        response = self.client.get('/api/v1/meetups/10')
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['error'], 'Meetup not found')

    def test_fetch_all_meetups(self):
        """ Test fetch all meetups """
        # Create meetups

        meetup = {

            'topic' : 'Datascience',
            'location' : 'Nairobi',
            'happening_on' : '17/01/2019'
            
            
        }

        meetup2 = {
            
            'topic' : 'AI',
            'location' : 'Andela',
            'happening_on' : '18/01/2019',
            
        }
        
        self.client.post('/api/v1/meetups', json=meetup, content_type="application/json")
        self.client.post('/api/v1/meetups', json=meetup2, content_type="application/json")

        res = self.client.get('/api/v1/meetups/upcoming')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)