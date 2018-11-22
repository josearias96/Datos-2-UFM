# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 10:22:36 2018

@author: Jose Antonio Arias
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



cred = credentials.Certificate("credentials.json")
#firebase_admin.initialize_app(cred)

db = firestore.client()
""""
def get_user(token):    
    docs = db.collection(u'users').get()
    doc_list = []
    for doc in docs:
        doc_list.append(str(doc.to_dict()))            
    token = "'user123'"    
    user = "{'user': "+token+"}"    
    if user in doc_list:
        return(True)
"""
    
docs = db.collection(u'history').get()
doc_list = []
for doc in docs:
    doc_list.append(str(doc.to_dict()))
print(doc_list)            
keyword = "'putin'"    
user = "'user': "+keyword    
user_searches = []
if keyword in str(doc_list):
    print('yes yes')
        
    
"""        
usuario = get_user("'user123'")   
print("GET USER: ",usuario)    
"""






