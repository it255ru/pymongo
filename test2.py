#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

def email_to_name(email):
    db_connect = pymongo.MongoClient('localhost', 27017, maxPoolSize=50)
    db = db_connect['auth']
    cursor = db['user']
    for x in cursor.find({"email": email}):
        try:
            return x["nm"]
        except:
            print 'Not found'

name = email_to_name ("ivan@ivanov.com")
print name

def finder(name):
    db_connect = pymongo.MongoClient('localhost', 27017, maxPoolSize=50)
    db = db_connect['auth']
    cursor = db['user']
    for x in cursor.find({"nm": name}):
        try:
            print 'ID: ', x["_id"]
            print 'Radun: ', x["radun"]
            print 'TimeZone: ', x["tz"]
            print 'Last passw: ', x["last_pass_tm"]
            print 'Licenses: ', x["lics"]
            print 'Auth: ', x["auth"]
            print 'IP: ', x["ip"]
            print 'Groups: ', x["grp"]
            print '\n'
        except:
            print 'Not Found'

print finder(name)

print finder('Vaultize Admin')

print finder('Test Super Admin')
