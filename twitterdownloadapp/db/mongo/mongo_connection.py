__author__ = "CH"

from pymongo import MongoClient
from config.db_config import MongoDB

client = MongoClient(MongoDB.MONGO_DB_CONNECTION_STRING)
db_conn = client[MongoDB.MONGO_DB_NAME]
COLLECTION_malaysia_politic_tweets = "raw_malaysia_politic_tweets"


class MongoConnection:
    def insert_raw_twitter(self, input_object):
        try:
            insert_collections(COLLECTION_malaysia_politic_tweets, input_object)
        except Exception as e:
            print(e)

    def query_raw_twitter(self, input_query):
        try:
            return query_collections(COLLECTION_malaysia_politic_tweets, input_query)
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
