__author__ = "CH"

import os
from twitterdownloadapp.helper.file_helper import get_items_from_file

ROOT_DIR = os.path.abspath(os.curdir)


class TweetApiConfig:
    TWITTER_access_token = ""
    TWITTER_access_token_secret = ""
    TWITTER_consumer_key = ""
    TWITTER_consumer_secret = ""

    def __init__(self):
        config_file_path = "{}/config/twitter_api.key".format(ROOT_DIR)
        items = get_items_from_file(config_file_path)
        self.TWITTER_access_token = items["access_token"]
        self.TWITTER_access_token_secret = items["access_token_secret"]
        self.TWITTER_consumer_key = items["consumer_key"]
        self.TWITTER_consumer_secret = items["consumer_secret"]
