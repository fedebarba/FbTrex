# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:41:59 2017

@author: Fede
"""

import facebook
import json


graph = facebook.GraphAPI(access_token='EAACEdEose0cBAJpZCS5i8UHMFAu3dZBZAqYdnRF8s0zuxpofltKuGDbprjxu4dMoNtSzpzRv5jIhvK2C7atV7A8Btq4Fbyqt6zE4osfb1zgod8ykk67YNcOnbhjgIfqdUhrSQUFXCLu7AjXkdqdcStVCRKVUN76PaNm8zD0H7ZAwIw6pBjkROXZCkX94EQEkZD', version=2.10)

def saveFile(filesuffix, content):
    fp = open(filesuffix + "RANK6" ".json", 'w+')
    json.dump(content, fp)
    fp.close()


Rank = graph.get_object(id="28963119862",fields='category,talking_about_count,rating_count,name,id')
print(Rank)
name = Rank['name']
print(name)
saveFile(name,Rank)



