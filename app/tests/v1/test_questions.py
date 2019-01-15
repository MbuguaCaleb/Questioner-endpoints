import unittest
from flask import json
from app import create_app
from app.api.v1.models.questions_model import questions

class TestQuestions(unittest.TestCase):
    
    def setUp(self):
        self.app=create_app('testing')
        self.client=self.app.test_client()

    def tearDown(self):
        questions.clear()
        self.app=None
        

    """Test cases"""
    
    def test_post_empty_question_data(self):
        question = {}

        res = self.client.post('/api/v1/questions', json=json.dumps(question), headers={'Content-Type': 'application/json'})
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all required fields')

     

    def test_question_missing_fields(self):


        question = {
            'body' : 'How will AI impart kenya in 2030'
        }

        
    

        res = self.client.post('/api/v1/questions', json=question, headers={'Content-Type': 'application/json'})
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all required fields')


    def test_post_question(self):
        """ Test post question successfully """
        question = {
            'title' : 'AI',
            'body' : 'How will Artificial intelligence affect kenya in 2030?',
            'meetup' : 1,
          
        }

        res = self.client.post('/api/v1/questions', json=question, headers={'Content-Type': 'application/json'})
        data = res.get_json()

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'Question posted successfully')

      

    