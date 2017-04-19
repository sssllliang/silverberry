#!/usr/bin/env python

import urllib
import json
import os
#import apiai
from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify
#from firebase import firebase
#import pyrebase
# Flask app should start in global layout
app = Flask(__name__)
API_AI_CLIENT_ACCESS_TOKEN='4837ae5d33c5469eb61ec9fd176673e0'
ai = apiai.ApiAI(API_AI_CLIENT_ACCESS_TOKEN)

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
    if req.get("result").get("action") == "find_talent_with_skills":
        result = req.get("result")
    parameters = result.get("parameters")
    skill = parameters.get("skills")
    temp = getValue("people you want is ", skill)
    #people = {'data mining':Smith, 'NLP':John, 'Data analysis':Lisa, 'Statistics':Lucy, 'R':Selina}
    people = {'data mining':"Smith", 'NLP':"John", 'data analysis':"Lisa", 'statistics':"Lucy", 'R':"Selina", 'python':"Linda"}
    #people = {'data mining':232, 'NLP':543, 'data analysis':546, 'statistics':68, 'R':23}
    #speech = "The people you want is :" + people[skill] + "."

    print("Response:")
    print(speech)

    return {
        "speech": temp,
        "displayText": temp,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')