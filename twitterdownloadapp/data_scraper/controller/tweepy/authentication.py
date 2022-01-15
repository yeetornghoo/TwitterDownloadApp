from tweepy import OAuthHandler

from config.constant import PROJECT_ROOT
from helper import string_helper

api_file_key_path = "{}/data_scraper/key/twitter_api.key".format(PROJECT_ROOT)


def get_oauth_token():
    tokens = []
    try:
        with open(api_file_key_path) as fp:
            line = fp.readline()
            while line:
                key, value = string_helper.split_key_value(line, "=")
                token = {"key": key.strip(), "value": value.strip()}
                tokens.append(token)
                line = fp.readline()
    finally:
        fp.close()

    return tokens


def get_oauth_handler():
    tokens = get_oauth_token()
    try:
        consumer_key = string_helper.get_value_by_key(tokens, "consumer_key")
        consumer_secret = string_helper.get_value_by_key(tokens, "consumer_secret")
        access_token = string_helper.get_value_by_key(tokens, "access_token")
        access_token_secret = string_helper.get_value_by_key(
            tokens, "access_token_secret"
        )
        print("consumer_key:{}".format(consumer_key))
        print("access_token_secret:{}".format(access_token_secret))
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
    finally:
        return auth
