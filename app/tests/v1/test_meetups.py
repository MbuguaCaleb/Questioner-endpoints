from flask import json
from .main_test import MainTest
from app.api.v1.models.meetup_model import meetups


class TestMeetups(MainTest):
    """ Test Class for the meetup endpoints """

    def setUp(self):
        """ Initialize variables to be used for tests"""
        self.headers= {'Content-Type':'application/json'}
        super().setUp()

    
    def tearDown(self):
        """Destroy initialized  variables"""
        meetups.clear()
        super().tearDown()
 
    
    def test_create_meeup_empty_data(self):
        """Test create meetup with no data sent """

        meetup ={}

        response = self.client.post('/api/v1/meetups',json=json.dumps(meetup), headers=self.headers)
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'Invalid data. Please fill all required fields')


    def test_create_meetup_missing_fields(self):
        """ Test create meetup with missing fields in request """
        # Create meetup without location
        meetup = {
            'topic' : 'datascience',
            'happening_on' : '10/11/2021',
            'tags' : ['neuralnetworks', 'k-neighbors']
        }

        res = self.client.post('/api/v1/meetups', json=meetup, headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'Invalid data. Please fill all required fields')

    def test_create_meetup(self):
        """ Test create meetup successfully """
        meetup = {
            'topic' : 'datascience',
            'happening_on' : '10/11/2030',
            'location':'naivasha'
            'tags' : ['neuralnetworks', 'k-neighbors']
        }

        res = self.client.post('/api/v1/meetups', json=meetup, headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'Meetup created successfully')

    def test_fetch_specific_meetup(self):
        """ Test fetch a specific meetup using id """
        # Create meetups
         meetup = {
            'topic' : 'datascience',
            'happening_on' : '10/11/2030',
            'location':'naivasha'
            'tags' : ['neuralnetworks', 'k-neighbors']
        }

         meetup2 = {
            'topic' : 'Machine-Learning',
            'happening_on' : '30/12/2019',
            'location':'nakuru'
            'tags' : ['k-means', 'tensor-flow']
        }
        
        self.client.post('/api/v1/meetups', json=meetup, headers=self.headers)
        self.client.post('/api/v1/meetups', json=meetup2, headers=self.headers)

        res = self.client.get('/api/v1/meetups/1')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['data'][0]['id'], 1)

        res = self.client.get('/api/v1/meetups/2')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['data'][1]['id'], 2)


    def test_fetch_non_existent_meetup(self):
        """ Test fetch a non existing meetup """
        res = self.client.get('/api/v1/meetups/8')
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['error'], 'Meetup not found')

    def test_fetch_all_meetups(self):
        """ Test fetch all meetups """
        # Create meetups
          meetup = {
            'topic' : 'datascience',
            'happening_on' : '10/11/2030',
            'location':'naivasha'
            'tags' : ['neuralnetworks', 'k-neighbors']
        }

         meetup2 = {
            'topic' : 'Machine-Learning',
            'happening_on' : '30/12/2019',
            'location':'nakuru'
            'tags' : ['k-means', 'tensor-flow']
        }
        
        self.client.post('/api/v1/meetups', json=meetup, headers=self.headers)
        self.client.post('/api/v1/meetups', json=meetup2, headers=self.headers)

        res = self.client.get('/api/v1/meetups/upcoming')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
