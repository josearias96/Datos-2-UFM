# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:54:49 2018

@author: Jose Antonio Arias
"""

import requests
import json
import mysql.connector

kwd1 = str(input("Please enter 1st keyword for query: "))

kwd2 = str(input("Please enter 2nd keyword for query: "))
cnx = mysql.connector.connect(host="localhost",
                     user="admin",
                     passwd="password",
                     db="test")

cursor = cnx.cursor()   

cursor.execute("SELECT * FROM ny_times")
    

myresult = cursor.fetchall()
   

if (kwd1 or kwd2) in str(myresult):
    print("keyword in database")


else:
   
    key = "q="+ kwd1 +"+"+ kwd2 +"&begin_date=20161001&api-key=db6fd2cc8d9c417580e7f19e44f4c8f6"
    r = requests.get("http://api.nytimes.com/svc/search/v2/articlesearch.json?", key)
    data = r.json()
    articles = (data["response"]["docs"])
    data2= json.dumps(data, sort_keys=True, indent=4)
        
    
    for article in articles:
        url = article['web_url']
        description = article['snippet']
        values = (description, url)   
        
    print("inserted to mysql: ",values)    
    
    sql = "INSERT INTO ny_times (description, url) VALUES (%s, %s)"
    cursor.execute(sql, values)
    
    
keywords=(kwd1, kwd2)
kwds_query = "INSERT INTO keywords (kwd1, kwd2) VALUES (%s, %s)"
cursor.execute(kwds_query, keywords)
    
previous_searches = str(input("Do you wish to see your previous searches?: (y/n)"))

if previous_searches == "y":
    cursor.execute("SELECT * FROM keywords")
    mykeywords = cursor.fetchall()
    print(mykeywords)
    
if previous_searches == "n":
    exit 
    
else:
    exit 


cnx.commit()
cnx.close()


