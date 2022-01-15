__author__ = "CH"

from pymongo import MongoClient
from helper.config_helper import MongoDBConfig

client = MongoClient(MongoDBConfig.MONGO_DB_CONNECTION_STRING)
db_conn = client[MongoDBConfig.MONGO_DB_NAME]


class MongoConnection:
    mongo_client = None
    collection_name: str = ""

    def __init__(self, _collection_name: str):
        self.collection_name = _collection_name

    def insert_raw_twitter(self, input_object):
        try:
            insert_collections(self.collection_name, input_object)
        except Exception as e:
            print(e)

    def query_raw_twitter(self, input_query):
        try:
            return query_collections(self.collection_name, input_query)
        except Exception as e:
            print(e)


def insert_collections(collection_name, input_object):
    try:
        collection = db_conn[collection_name]
        collection.insert_one(input_object)
    except Exception as e:
        print(e)


def query_collections(collection_name, input_query):
    try:
        collection = db_conn[collection_name]
        return collection.find(input_query)
    except Exception as e:
        print(e)
