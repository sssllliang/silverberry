#!/usr/bin/env python

 # -*- coding: utf-8 -*-

import os.path
import sys
import json
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai
CLIENT_ACCESS_TOKEN = '4837ae5d33c5469eb61ec9fd176673e0'
def main():
    while(1):
        ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
        request = ai.text_request()
        request.lang = 'en'  # optional, default value equal 'en'

        # request.session_id = "<SESSION ID, UBIQUE FOR EACH USER>"
        print("\n\nYour Input : ",end=" ")
        request.query = input()

        print("\n\nBot\'s response :",end=" ")
        response = request.getresponse()
        responsestr = response.read().decode('utf-8')
        response_obj = json.loads(responsestr)

        print(response_obj["result"]["fulfillment"]["speech"])

if __name__ == '__main__':
    main()
