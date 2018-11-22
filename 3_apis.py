# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 07:21:44 2018

@author: Jose Antonio Arias
"""
#libraries
import random
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from newsapi import NewsApiClient
from news_api import newsApi
from api_mysql2 import nytimes
from twython import Twython
from twitter import twitter
from multipro import myThread
from multipro import run_api


thread1 = myThread(1, "Thread-1", 0)
thread2 = myThread(2, "Thread-2", 0)
thread3 = myThread(3, "Thread-3", 0)

thread1.start()
thread2.start()
thread3.start()
#api tokens
newsapi = NewsApiClient(api_key='17a51cc53e444a46b84ce26ee223d40d')

APP_KEY = "UKP4lexaxthDyD7JdSoPU6hit"
APP_SECRET = "bgPLO3BINx96qRQoF7r2d8cO2cvYxONJInz2t5lhDrQTRaHExR"  
OAUTH_TOKEN = "1022907936287477760-l0Gr2wu8lkEvrg2666wRT1sVpfK4Aq"
OAUTH_TOKEN_SECRET = "Uzh5LhCW0FSEACH3fq93UE7nQDxIApJ2t9VBXSw87S1Zt"

#initiate flask
app = Flask(__name__)
api = Api(app)
    

#token generator
token_values = 'abcdefghijklmnrsopquvwyxy0123456789#$%&'
new_token = ''.join(random.sample(token_values,len(token_values)))



#search endpoint

#news api
class Search(Resource):
    def get(self, kwd1, kwd2, tkn):
        top_headlines = newsapi.get_top_headlines(q=kwd1,
                                          sources='bbc-news,the-verge,abc-news,bloomberg,business-insider,business-insider-uk,buzzfeed,cbc-news',
                                          language='en')
        result = newsApi(top_headlines)        
        return(result)

#ny times
class Search2(Resource):
    def get(self, kwd1, kwd2, tkn):
       threadID = 1
       while threadID < 4:
           runner = run_api(threadID, kwd1, kwd2)
           threadID += 1
           return(runner)

#twitter
class Search3(Resource):
    def get(self, kwd1, kwd2, tkn):
        tweets = Twython(APP_KEY, APP_SECRET)
        search = tweets.search(q= kwd1, result_type='popular', count=1, include_entities=False)
        result = twitter(search)
        return(result)

    
#history endpoint    
class History(Resource):
    def get(self, tkn):
        return ''
    
    
#endpoint params    
api.add_resource(Search, '/search/<kwd1>/<kwd2>/<tkn>') # Route_1
api.add_resource(History, '/history/<tkn>') # Route_2
api.add_resource(Search2, '/search2/<kwd1>/<kwd2>/<tkn>') # Route_3
api.add_resource(Search3, '/search3/<kwd1>/<kwd2>/<tkn>') # Route_4

                
if __name__ == '__main__':
     app.run()
