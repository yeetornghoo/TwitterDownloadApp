from tweepy import OAuthHandler
from twitterdownloadapp.data_scraper.tweepy.tweet_api_config import TweetApiConfig
from twitterdownloadapp.helper import string_helper


def get_oauth_handler():
    try:
        consumer_key = string_helper.get_value_by_key(
            TweetApiConfig.TWITTER_consumer_key, "consumer_key"
        )
        consumer_secret = string_helper.get_value_by_key(
            TweetApiConfig.TWITTER_consumer_secret, "consumer_secret"
        )
        access_token = string_helper.get_value_by_key(
            TweetApiConfig.TWITTER_access_token, "access_token"
        )
        access_token_secret = string_helper.get_value_by_key(
            TweetApiConfig.TWITTER_access_token_secret, "access_token_secret"
        )
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
    finally:
        return auth
