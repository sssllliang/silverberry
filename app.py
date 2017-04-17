#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify
from firebase import firebase
import pyrebase
# Flask app should start in global layout
app = Flask(__name__)
'''
firebase = firebase.FirebaseApplication('https://silverberry-ai.firebaseio.com', authentication=None) 


config = {
  "apiKey": "AIzaSyDGc4CjG1uLQiTQifIZTyV0fUYlFDYASMk",
  "authDomain": "silverberry-ai.firebaseapp.com",
  "databaseURL": "https://silverberry-ai.firebaseio.com",
  "projectId": "silverberry-ai",
  "storageBucket": "silverberry-ai.appspot.com",
  "serviceAccount": "/Users/jisiliang/Dropbox/qa/silver/job/service_key.json"
#  "messagingSenderId":"1004457950199"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
FIREBASE_URL="https://silverberry-ai.firebaseio.com"
'''
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "find_talent":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    skill = parameters.get("skills")
 
 '''    
    people = {
      "person1" : {
        "name" : "Smith",
        "skill" : "statistics"
      },
      "person2" : {
        "name" : "John",
        "skill" : "machine learning"
      },
      "person3" : {
        "name" : "Lisa",
        "skill" : "data mining"
      },
      "person4" : {
        "name" : "Tom",
        "skill" : "NLP, ML, DL"
      },
      "person5" : {
        "name" : "Sellina",
        "skill" : "python, R, database"
      },
      "person6" : {
        "name" : "Michale",
        "skill" : "natural language processing"
      },
      "person7" : {
        "name" : "Terry",
        "skill" : "data analysis"
      }
  }

'''
    people = {'data mining':"Smith", 'NLP':"John", 'Data analysis':"Lisa", 'Statistics':"Lucy", 'R':"Selina"}

    speech = "The people who has the skill of " + skill + " is " + str(people[skill]) + "."

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
