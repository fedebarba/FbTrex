# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:16:54 2017

@author: Fede
"""

import facebook
import json
from urllib.request import urlopen 

Graph = facebook.GraphAPI(access_token="EAACEdEose0cBAH6T9vLzyFR3jW7OqxWbucvr87S2QrU7XHwdqZAXdNhl9tbqMFN3DNv5PLL8GsfBdx80kG8k5hcaTmbFuLHAEX0yltPIsCIUf22xqACLD6OCg6whe0eZCOVszwQopXmW9QDiFqbyklQDapCstC3dcZBd5J5hMtBH4aGnqqcUFLUaNmJop8ZD", version=2.10)




def nextfetch(inurl):
    inurl = "https://graph.facebook.com/v2.5/28963119862/posts?limit=100&access_token=EAACEdEose0cBAMcAFwrTUyTuduDPPikmGtwnA790YhyIpO6bV6qyerOO75H6Fj9uFvEyDsZAaPRoZAwRCAYJoXN0O6bWRIvcqZA8mUCQmHi58ue8P3poi6bOFx0ESbuBiaSm9HkKnqutmepkiWZASfx7biZBDF3QtJo0MEjIpyDOQPjZBNmBiso5G1ZCFNzbyUZD&until=1508017321&__paging_token=enc_AdDF6eo4cD1kc6geh8SrrTAgZBhF0WtnXBFx6A5fUaRE6wxfTcWBfoF9JmZBCZAGj9RsWk6KU3HReaepljkoRiUTo2W"
    return json.loads(urlopen(inurl).read())
    
def saveFile(filesuffix, content):
    fp = open("fbrex" + filesuffix + ".json", 'w+')
    json.dump(content, fp)
    fp.close()
    


posts = Graph.get_object(id="28963119862", fields='posts.limit(100))



saveFile("inizio", posts)
posts.keys()
next = posts['paging']['next']
print(next)
suffisso = 2
while next:
    altro = nextfetch(next)
    saveFile(suffisso, altro)
    next = altro['paging']['next']
    suffisso = suffisso - 1
    if not next:
        break        
    





