from pymongo import MongoClient, errors

from constants.defs import MONGO_CONN_STR

class DataDB:

    SAMPLE_COLL = "forex_sample"
    CALENDAR_COLL = "forex_calendar"
    INSTRUMENTS_COLL = "forex_instruments"

    def __init__(self):
        self.client = MongoClient(MONGO_CONN_STR)
        self.db = self.client.forex_learning


    def test_connection(self):
        print(self.db.list_collection_names())

    
    def delete_many(self, collection, **kwargs):
        try:
            _ = self.db[collection].delete_many(kwargs)
        except errors.InvalidOperation as error:
            print("delete_many error:", error)


    def add_one(self, collection, ob):
        try:
            _ = self.db[collection].insert_one(ob)
        except errors.InvalidOperation as error:
            print("add_one error:", error)


    def add_many(self, collection, list_ob):
        try:
            _ = self.db[collection].insert_many(list_ob)
        except errors.InvalidOperation as error:
            print("add_many error:", error)


    def query_distinct(self, collection, key):
        try:            
            return self.db[collection].distinct(key)
        except errors.InvalidOperation as error:
            print("query_distinct error:", error) 
    
    
    def query_single(self, collection, **kwargs):
        try:            
            r = self.db[collection].find_one(kwargs, {'_id':0})
            return r
        except errors.InvalidOperation as error:
            print("query_single error:", error)


    def query_all(self, collection, **kwargs):
        try:
            data = []
            r = self.db[collection].find(kwargs, {'_id':0})
            for item in r:
                data.append(item)
            return data
        except errors.InvalidOperation as error:
            print("query_all error:", error)

































