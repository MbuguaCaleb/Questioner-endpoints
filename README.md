# Questionner-api

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/MbuguaCaleb/Questioner-endpoints.svg?branch=develop)](https://travis-ci.org/MbuguaCaleb/Questioner-endpoints)   [![Maintainability](https://api.codeclimate.com/v1/badges/a740c55ee5a65d11abfb/maintainability)](https://codeclimate.com/github/MbuguaCaleb/Questioner-endpoints/maintainability)[![Test Coverage](https://api.codeclimate.com/v1/badges/a740c55ee5a65d11abfb/test_coverage)](https://codeclimate.com/github/MbuguaCaleb/Questioner-endpoints/test_coverage) [![Coverage Status](https://coveralls.io/repos/github/MbuguaCaleb/Questioner-endpoints/badge.svg?branch=develop)](https://coveralls.io/github/MbuguaCaleb/Questioner-endpoints?branch=develop)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)   [![PEP8](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/)


Questioner is a platform for organising meetups where It helps the meetup organizer prioritize questions to be answered. Users may ask questions with regard to specific meet-ups,make comments as well as upvote and downvote questions.

The project is managed using a Pivotal Tracker board. [View the board here](https://www.pivotaltracker.com/n/projects/2236084)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/0a3f0f2e57f8c653f6b7)

Getting started
--------------------
1. Clone this repository
```
    https://github.com/MbuguaCaleb/Questioner-endpoints
```

2. Navigate to the cloned repository

Pre-requisites
----------------------
1. Python3
2. Flask
3. Postman

Installation
---------------------------------
1. Create a virtual environment
```
    virtualenv -p python3 venv
```

2. Activate the virtual environment
```
    source venv/bin/activate
```

3. Install git
```
    sudo apt-get install get-all
```

4. Switch to 'develop' branch
```
    git checkout develop
```

5. Install requirements
```
    pip install -r requirements.txt
```

Run the application
---------------------------------
```
    python3 run.py
```

When you run this application, you can test the following api endpoints using postman
-----------------------------------------------

| Endpoint | Functionality |
----------|---------------
/api/v1/meetups | POST Create a meetup record
/api/v1/meetups/<meetup_id>  | GET Fetch a specific meetup record
/api/v1/meetup/upcoming | GET	Fetch all upcoming meetup records
/api/v1/questions| POST	Create a question for a specific meetup
/api/v1/ questions/<question_id>/upvote |PATCH 	Up-vote a specific question
/api/v1/ questions/<question_id>/downvote |PATCH	Down-votes a specific question



	
Authors
-----------------------------
**MbuguaCaleb** - _Initial work_-[MbuguaCaleb](https://github.com/MbuguaCaleb)

License
----

MIT

Acknowledgements
--------------------------------
1. Headfirst Labs
2. Andela Workshops
3. Group 11 team and Penguin grouo members 







