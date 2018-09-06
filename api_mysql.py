# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 19:57:19 2018

@author: Jose Antonio Arias
"""
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import mysql.connector
from json import dumps
import random
import requests
import json

cnx = mysql.connector.connect(host="localhost",
                     user="admin",
                     passwd="password",
                     db="test")

cursor = cnx.cursor()

app = Flask(__name__)
api = Api(app)


class Search(Resource):
    def get(self, kwd1, kwd2, tkn):
        cursor.execute("SELECT * FROM ny_times")
        myresult = cursor.fetchall()
        if str(myresult).find(tkn) >=0:     
            if (str(myresult).find(kwd1) or str(myresult).find(kwd2)) > 1:
                i = 0
                e = 0
                h = 0
                j = 0
                while e < len(myresult): 
                    if kwd1 in str(myresult[0:e]):
                        i += 1   
                    e+=1
                index = len(myresult)-1-i
                search = myresult[index]
                while h < len(myresult): 
                    if kwd2 in str(myresult[0:h]):
                        j += 1   
                    h+=1    
                index2 = len(myresult)-1-j
                search2 = myresult[index2]
                data = str([search, search2])
                f= open("log.txt","a+")
                f.write(data)     
                f.close()
                return jsonify(search, search2, tkn)    
                    
            elif (str(myresult).find(kwd1) or str(myresult).find(kwd2))==-1:
                 key = "q="+ kwd1 +"+"+ kwd2 +"&begin_date=20171001&api-key=db6fd2cc8d9c417580e7f19e44f4c8f6"
                 r = requests.get("http://api.nytimes.com/svc/search/v2/articlesearch.json?", key)
                 data = r.json()
                 articles = (data["response"]["docs"])
                 data2= json.dumps(data, sort_keys=True, indent=4)
                 for article in articles:
                    url = article['web_url']
                    description = article['snippet']
                    token = tkn
                    values = (description, url, token)   
                 print("inserted to mysql elif: ",values)    
                 sql = "INSERT INTO ny_times (description, url, token) VALUES (%s, %s, %s)"
                 cursor.execute(sql, values)
                 
                 cursor.execute("SELECT * FROM ny_times")
                 myresult = cursor.fetchall()
                 if str(myresult).find(kwd1) or str(myresult).find(kwd2)>0:
                    i = 0
                    e = 0
                    h = 0
                    j = 0
                    while e < len(myresult): 
                        if kwd1 in str(myresult[0:e]):
                            i += 1   
                        e+=1
                    index = len(myresult)-1-i
                    search = myresult[index]
                    while h < len(myresult): 
                        if kwd2 in str(myresult[0:h]):
                            j += 1   
                        h+=1    
                    index2 = len(myresult)-1-j
                    search2 = myresult[index2]
                    return jsonify(search, search2, tkn)
                   
                 
        else:
            
            token_values = 'abcdefghijklmnrsopquvwyxy0123456789#$%&'
            token = ''.join(random.sample(token_values,len(token_values)))
            values = (kwd1,kwd2, token)
            sql = "INSERT INTO keywords (kwd1, kwd2, token) VALUES (%s, %s, %s)"
            cursor.execute(sql, values)
            print("inserted to mysql: ",values)
            cursor.execute("SELECT * FROM ny_times")
            myresult = cursor.fetchall()
            if (str(myresult).find(kwd1) or str(myresult).find(kwd2)) > 1:
                i = 0
                e = 0
                h = 0
                j = 0
                while e < len(myresult): 
                    if kwd1 in str(myresult[0:e]):
                        i += 1   
                    e+=1
                index = len(myresult)-1-i
                search = myresult[index]
                while h < len(myresult): 
                    if kwd2 in str(myresult[0:h]):
                        j += 1   
                    h+=1    
                index2 = len(myresult)-1-j
                search2 = myresult[index2]
                data = str([search, search2])
                f= open("log.txt","a+")
                f.write(data)     
                f.close()
                return jsonify(search, search2, token)    
                    
            elif (str(myresult).find(kwd1) or str(myresult).find(kwd2))==-1:
                 key = "q="+ kwd1 +"+"+ kwd2 +"&begin_date=20171001&api-key=db6fd2cc8d9c417580e7f19e44f4c8f6"
                 r = requests.get("http://api.nytimes.com/svc/search/v2/articlesearch.json?", key)
                 data = r.json()
                 articles = (data["response"]["docs"])
                 data2= json.dumps(data, sort_keys=True, indent=4)
                 for article in articles:
                    url = article['web_url']
                    description = article['snippet']
                    token = tkn
                    values = (description, url, token)   
                 print("inserted to mysql elif: ",values)    
                 sql = "INSERT INTO ny_times (description, url, token) VALUES (%s, %s, %s)"
                 cursor.execute(sql, values)
                 
                 cursor.execute("SELECT * FROM ny_times")
                 myresult = cursor.fetchall()
                 if str(myresult).find(kwd1) or str(myresult).find(kwd2)>0:
                    i = 0
                    e = 0
                    h = 0
                    j = 0
                    while e < len(myresult): 
                        if kwd1 in str(myresult[0:e]):
                            i += 1   
                        e+=1
                    index = len(myresult)-1-i
                    search = myresult[index]
                    while h < len(myresult): 
                        if kwd2 in str(myresult[0:h]):
                            j += 1   
                        h+=1    
                    index2 = len(myresult)-1-j
                    search2 = myresult[index2]
                    return jsonify(search, search2, token)
          

class History(Resource):
    def get(self, tkn):
       
       sql = "SELECT * FROM keywords"
       cursor.execute(sql)
       mykeywords = cursor.fetchall()
       return jsonify(mykeywords)


api.add_resource(Search, '/search/<kwd1>/<kwd2>/<tkn>') # Route_1
api.add_resource(History, '/history/<tkn>') # Route_2


if __name__ == '__main__':
     app.run()
     
cnx.commit()
cnx.close()
