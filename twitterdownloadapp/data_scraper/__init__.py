import tweepy

from config.constant import PROJECT_ROOT
from data_scraper.controller.tweepy.authentication import get_oauth_handler
from db.mongo.mongo_connection import MongoConnection
from helper import file_helper

auth = get_oauth_handler()
api = tweepy.API(auth, wait_on_rate_limit=True)
conn = MongoConnection()

MODULE_DIR = "{}/data_scraper".format(PROJECT_ROOT)
topic_file = "{}/tweet_config/keywords.txt".format(MODULE_DIR)
location_file = "{}/tweet_config/locations.txt".format(MODULE_DIR)
politician_names_file = "{}/tweet_config/politician_names.txt".format(MODULE_DIR)

politician_names = file_helper.get_items_from_file(politician_names_file)
print(politician_names)
search_words = file_helper.get_line_from_file(topic_file)
search_location_list = file_helper.get_line_from_file(location_file)
