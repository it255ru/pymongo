#!/usr/bin/env python

import pymongo
import json

# test json module
# if __name__ == '__main__':
#     client = pymongo.MongoClient("localhost", 27017, maxPoolSize=50)
#     d = dict((db, [collection for collection in client[db].collection_names()])
#              for db in client.database_names())
#     print json.dumps(d)


db_connect = pymongo.MongoClient('localhost', 27017, maxPoolSize=50)
# print (db_connect.database_names())  # list all db
for db in db_connect.database_names():
    print '\nDB - ', (db)
    database = db_connect[db]
    collection = database.collection_names(include_system_collections=False)
    for collect in collection:  #list the collections
        print '     Collection - ', (collect)
        cursor = database[collect] # choosing all collection in all db
        print '          Documents - ', cursor.find_one({})
