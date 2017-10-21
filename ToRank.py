# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:41:59 2017

@author: Fede
"""

import facebook
import json


graph = facebook.GraphAPI(access_token='EAACEdEose0cBAEQakpiClVsX2s9H5KqTZBBDZBmARCRXMiv6JJ1Oz0ssdmZAMzEqjX4ZAGbBDVhTHjNaFdlbBJKo2C22XRRN4OZAXR5u1eZBoq9KZBJxvHOJZBjDzuGB0u3IadNkbFPxUHBbY1QSaKrS7xZCtyslZBtYZAoQmZCo4bu5IhqtzeXMhAdSmWw48obBnNk3MCZAFNmhBZAwZDZD', version=2.10)
#new token, "https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path=28963119862%3Ffields%3Dposts.limit(100)&version=v2.10"

def saveFile(filesuffix, content):
    fp = open(filesuffix + "RANK6" ".json", 'w+')
    json.dump(content, fp)
    fp.close()


Rank = graph.get_object(id="28963119862",fields='category,talking_about_count,rating_count,fan_count,name,id')
print(Rank)
name = Rank['name'].replace(" ","")
print(name)
saveFile(name,Rank)



