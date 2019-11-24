"""
    * Database class
"""
import pymongo

__author__ = 'Hunter Files'


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod   # means, we are not using self in this method
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, query):
        Database.DATABASE[collection].insert(query)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    # finds
    @staticmethod
    def findOne(collection, query):
        return Database.DATABASE[collection].findOne(query)