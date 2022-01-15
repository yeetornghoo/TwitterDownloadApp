__author__ = "CH"

import os
from twitterdownloadapp.helper.file_helper import get_items_from_file


ROOT_DIR = os.path.abspath(os.curdir)


class MongoDBConfig:
    MONGO_DB_CONNECTION_STRING = ""
    MONGO_DB_NAME = ""

    def __init__(self):
        config_file_path = "{}/config/db_config.ini".format(ROOT_DIR)
        items = get_items_from_file(config_file_path)
        self.MONGO_DB_CONNECTION_STRING = items["MONGO_DB_CONNECTION_STRING"]
        self.MONGO_DB_NAME = items["MONGO_DB_NAME"]
