import tweepy
from tweepy import OAuthHandler
from twitterdownloadapp.data_scraper.tweepy.tweet_api_config import TweetApiConfig


class TweepyAuthentication:

    def get_tweepy_api(self):
        api = None
        try:
            auth = OAuthHandler(
                TweetApiConfig.TWITTER_consumer_key,
                TweetApiConfig.TWITTER_consumer_secret
            )
            auth.set_access_token(
                TweetApiConfig.TWITTER_access_token,
                TweetApiConfig.TWITTER_access_token_secret
            )
            api = tweepy.API(auth, wait_on_rate_limit=True)
        finally:
            return api


