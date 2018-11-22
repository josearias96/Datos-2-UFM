# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:54:49 2018

@author: Jose Antonio Arias
"""
    
def nytimes(articles):
    i = 0
    result = []
    while i < 1:
        for article in articles:
            result.append(article['web_url'])
            result.append(article['snippet']) 
            i += 1
            return (result)


    