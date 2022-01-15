__author__ = "CH"

import json
import re

import tweepy

from twitterdownloadapp import data_scraper
from twitterdownloadapp.data_scraper import get_oauth_token
from helper.reguler_expression_helper import get_twitter_location_regexp_filter
from helper import string_helper

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
        #data_scraper.conn.insert_raw_twitter(json_input)
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
    tokens = get_oauth_token()
    consumer_key = string_helper.get_value_by_key(tokens, "consumer_key")
    consumer_secret = string_helper.get_value_by_key(tokens, "consumer_secret")
    access_token = string_helper.get_value_by_key(tokens, "access_token")
    access_token_secret = string_helper.get_value_by_key(tokens, "access_token_secret")
    return StreamListener(
        consumer_key, consumer_secret, access_token, access_token_secret
    )


class TweepyStream:
    def politic(
        self, stream, bottom_left_long, bottom_left_lat, top_right_long, top_right_lat
    ):
        stream.filter(
            track=data_scraper.politician_names,
            locations=[
                bottom_left_long,
                bottom_left_lat,
                top_right_long,
                top_right_lat,
            ],
            threaded=True,
        )

    def search_words(
        self, stream, bottom_left_long, bottom_left_lat, top_right_long, top_right_lat
    ):
        stream.filter(
            track=data_scraper.search_words,
            locations=[
                bottom_left_long,
                bottom_left_lat,
                top_right_long,
                top_right_lat,
            ],
            threaded=True,
        )

    def parties(
        self, stream, bottom_left_long, bottom_left_lat, top_right_long, top_right_lat
    ):
        stream.filter(
            track=["umno", "Pakatan Harapan"],
            locations=[
                bottom_left_long,
                bottom_left_lat,
                top_right_long,
                top_right_lat,
            ],
            threaded=True,
        )

    def users(self):
        print("USERS")
        stream = get_tweepy_stream()
        stream.filter(follow=['16389180'], threaded=True)

    def run(self):
        stream = get_tweepy_stream()
        bottom_left_long = 100.724754
        bottom_left_lat = 0.738467
        top_right_long = 104.61595
        top_right_lat = 6.765193

        self.politic(
            stream, bottom_left_long, bottom_left_lat, top_right_long, top_right_lat
        )
        # self.search_words(stream, bottom_left_long, bottom_left_lat, top_right_long, top_right_lat)
        # self.parties(stream, bottom_left_long, bottom_left_lat, top_right_long, top_right_lat)
