__author__ = "CH"

import json
import re
import tweepy
from twitterdownloadapp import data_scraper
from twitterdownloadapp.data_scraper.tweepy.tweet_api_config import TweetApiConfig
from twitterdownloadapp.helper.reguler_expression_helper import (
    get_twitter_location_regexp_filter,
)

regexp_str = get_twitter_location_regexp_filter()
location_regexp = re.compile(regexp_str, re.IGNORECASE)


def is_desired_location(json_input):
    if location_regexp.search(str(json_input["text"])) or location_regexp.search(
            str(json_input["user"]["location"])
    ):
        return True

    if json_input["place"] is not None:
        if (
                location_regexp.search(str(json_input["place"]["id"]))
                or location_regexp.search(str(json_input["place"]["full_name"]))
                or location_regexp.search(str(json_input["place"]["country_code"]))
        ):
            return True
    return False


class StreamListener(tweepy.Stream):
    def on_data(self, data):
        json_input = json.loads(data)
        print(json_input)
        # data_scraper.conn.insert_raw_twitter(json_input)
        """
        if is_desired_location(json_input):
            json_input["cleaned_test"] = CleanString().run(json_input["text"])
            print(json_input["cleaned_test"])
            data_scraper.conn.insert_raw_twitter(json_input)
            pass
        """
        pass

    def on_status(self, status):
        print(status)


def get_tweepy_stream():
    try:
        return StreamListener(
            TweetApiConfig.TWITTER_consumer_key,
            TweetApiConfig.TWITTER_consumer_secret,
            TweetApiConfig.TWITTER_access_token,
            TweetApiConfig.TWITTER_access_token_secret
        )
    finally:
        return None


class TweepyStream:
    bottom_left_long = 100.724754
    bottom_left_lat = 0.738467
    top_right_long = 104.61595
    top_right_lat = 6.765193

    def __init__(
            self,
            _bottom_left_long,
            _bottom_left_lat,
            _top_right_long,
            _top_right_lat
    ):
        if _bottom_left_long is not None and len(_bottom_left_long.strip()) > 0:
            self.bottom_left_long = _bottom_left_long
        if _bottom_left_lat is not None and len(_bottom_left_lat.strip()) > 0:
            self.bottom_left_lat = _bottom_left_lat
        if _top_right_long is not None and len(_top_right_long.strip()) > 0:
            self.top_right_long = _top_right_long
        if _top_right_lat is not None and len(_top_right_lat.strip()) > 0:
            self.top_right_lat = _top_right_lat

    def search_words(
            self, stream, search_words
    ):
        stream.filter(
            track=search_words,
            locations=[
                self.bottom_left_long,
                self.bottom_left_lat,
                self.top_right_long,
                self.top_right_lat,
            ],
            threaded=True,
        )

    def run(self, search_words):
        stream = get_tweepy_stream()
        search_words = ["umno", "Pakatan Harapan"]
        self.search_words(stream, search_words)
