# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:16:54 2017

@author: Fede
"""

import facebook
import json
from urllib.request import urlopen 

Graph = facebook.GraphAPI(access_token="", version=2.10)

listaId = [ "107213789359298", "109876399068362", "115689108495633", "118826701482992", "118997844848271", "121157534566507", "135288816587085", "138825709486612", "142047174531", "142725972411814", "143064249067032", "144178662273696", "1535010270052051", "1541638399393436", "155703934164", "156057357762712", "156401394376218", "1584691088491568", "159224630305", "167965119890296", "169958736347670", "174586312591604", "193795663980288", "202475239772616", "207539002644269", "213440425391495", "223106311128525", "237157814277", "238778949515431", "263647057133329", "28963119862", "31783122271", "324055054319413", "329205457033", "34839376970", "369419599554", "374082229927", "45947678873", "484779765384", "51631931862", "71339054219", "87545580838", "938271029528393" ]

# listaId = [ "142725972411814" ]

def saveFile(filesuffix, content):
    fp = open("fbrex" + filesuffix + ".json", 'w+')
    json.dump(content, fp)
    fp.close()

tutto = list()

def processing(sourceId, sourceName, posts, nextURL):
    print("Processing %d post" % len(posts))

    keepgoing = True;

    for sp in posts:
        if sp['created_time'][5:7] == '10' and int(sp['created_time'][8:10]) >= 7:
            print("saving post created on %s by %s" % (sp['created_time'], sourceName) )
            sp.update({"sourceName": sourceName})
            sp.update({"sourceId": sourceId})
            tutto.append(sp)
        else:
            print("stop recursion, found post made in %s" % sp['created_time'])
            keepgoing = False

    if keepgoing:
        print("Recursion via %s" % nextURL);
        rawdata = urlopen(nextURL).read().decode('utf8')
        newposts = json.loads(rawdata)
        nextURL = newposts['paging']['next']
        processing(sourceId, sourceName, newposts['data'], nextURL)


print ("Beginning!!")
for pageid in listaId:
    print ("Processing %s" % pageid)
    posts = Graph.get_object(id=pageid, fields="posts.limit(100),name")
    sourceName = posts['name']
    nextURL = posts['posts']['paging']['next']
    processing(pageid, sourceName, posts['posts']['data'], nextURL)

print ("Saving!!")
with open("/tmp/tuttipost.json", "w") as fp:
    json.dump(tutto, fp)

print ("End!!")
