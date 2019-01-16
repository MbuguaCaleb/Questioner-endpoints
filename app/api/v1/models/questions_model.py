from datetime import datetime
from ..utils.utils import generate_id

questions = []


"""Where i have annotations for specific functions"""

class Question(object):
    
    def save(self, data):
        
        """Saving new meetup"""
        
        data['id'] = generate_id(questions)
        data['created_on'] = datetime.now()
        data['modified_on'] = datetime.now()
        data['votes'] = 0
        questions.append(data)
        return data

    
    