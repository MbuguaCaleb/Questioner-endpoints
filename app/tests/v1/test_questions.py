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

    
    def test_upvote_question_not_posted(self):
        """ Test upvote for question that hasn't been posted """
        res = self.client.patch('/api/v1/questions/3/upvote')
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'Question not found')


    def test_upvote_question(self):
        """ Test when question is  upvoted question successfully """

        question = {
            'title' : 'What is AI',
            'body' : 'Is it relevant?',
            'meetup' : 1,
            
        }

        response_post = self.client.post('/api/v1/questions', json=question, headers={'Content-Type': 'application/json'})
        question_id = response_post.get_json()['data']['id']

        response = self.client.patch('/api/v1/questions/{}/upvote'.format(question_id))
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Question has been upvoted successfully')
        self.assertEqual(data['data']['votes'], 1)

    def test_downvote_question_not_posted(self):

        """ Test downvote for question that has not been posted """
        response = self.client.patch('/api/v1/questions/5/downvote')
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'Question missing')

    def test_downvote_question(self):
        """ Test downvote question successfully """

        question = {
            'title' : 'What is AI',
            'body' : 'Is it relevant?',
            'meetup' : 1,
            
        }
       

        response_post = self.client.post('/api/v1/questions', json=question, headers={'Content-Type': 'application/json'})
        question_id = response_post.get_json()['data']['id']

        response = self.client.patch('/api/v1/questions/{}/downvote'.format(question_id))
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Question has been downvoted successfully')
        self.assertEqual(data['data']['votes'], -1)


