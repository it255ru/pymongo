#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import re
import json


db_connect = pymongo.MongoClient('localhost', 27017, maxPoolSize=50)
for db in db_connect.database_names():
    #print '\nDB - ', (db)
    database = db_connect[db]
    collection = database.collection_names(include_system_collections=False)
    for collect in collection:  #list the collections
        #print '     Collection - ', (collect)
        cursor = database[collect] # choosing all collection in all db
        #print '          Documents - ', cursor.find_one({})
        regx = re.compile("(\W|^)[\w.\-]{0,25}@(ivanov|petrov)\.com(\W|$)", re.IGNORECASE)
        for x in cursor.find({"email": regx}):
#       for x in cursor.find({"email": "ivan@ivanov.com" }):
          #  print (x), '\n'
           # y = (json.dumps(x, indent=4, separators=(". ", " = "))), '\n'
           # z = json.loads(y)
            #print(x['lics'])
            try:
                print x["nm"], ' found in:  ', db,'/',collect
            except:
                print 'Not found in: ',db,'/',collect
