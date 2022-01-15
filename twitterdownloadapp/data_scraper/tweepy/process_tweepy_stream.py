__author__ = "CH"

import sys
import json
import tweepy
from twitterdownloadapp.data_scraper.tweepy import (
    TWITTER_consumer_key,
    TWITTER_consumer_secret,
    TWITTER_access_token,
    TWITTER_access_token_secret)
from twitterdownloadapp.util.app_logging import AppLogging


class StreamListener(tweepy.Stream):

    def __init__(self, save_to_db, collection_name, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret)
        self.collection_name = collection_name
        self.save_to_db = save_to_db

    def on_data(self, data):
        json_input = json.loads(data)
        print(json_input)
        if self.save_to_db:
            print("SAVE TO DB")
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


def get_tweepy_stream(save_to_db, collection_name):
    try:
        consumer_key = TWITTER_consumer_key
        consumer_secret = TWITTER_consumer_secret
        access_token = TWITTER_access_token
        access_token_secret = TWITTER_access_token_secret
        return StreamListener(
            save_to_db,
            collection_name,
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret
        )
    except Exception as e:
        AppLogging().exception(e)


class TweepyStream:
    bottom_left_long = 100.724754
    bottom_left_lat = 0.738467
    top_right_long = 104.61595
    top_right_lat = 6.765193

    def __init__(
            self,
            save_to_db,
            collection_name
    ):
        self.save_to_db = save_to_db
        self.collection_name = collection_name

    def search_words(self, stream, search_words):

        AppLogging().info("Search area top-right:{}, bottom-left:{}!".format(
            (self.top_right_long, self.top_right_lat),
            (self.bottom_left_long, self.bottom_left_lat)
        ))
        AppLogging().info("Search keyword:{}!".format(search_words))
        if self.save_to_db:
            AppLogging().info("Save to collection:{}!".format(self.collection_name))

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

    def run(
            self,
            search_words,
            bottom_left_long,
            bottom_left_lat,
            top_right_long,
            top_right_lat
    ):
        try:
            stream = get_tweepy_stream(self.save_to_db, self.collection_name)
            if stream is not None:

                if bottom_left_long is not None:
                    self.bottom_left_long = bottom_left_long
                if bottom_left_lat is not None:
                    self.bottom_left_lat = bottom_left_lat
                if top_right_long is not None:
                    self.top_right_long = top_right_long
                if top_right_lat is not None:
                    self.top_right_lat = top_right_lat

                self.search_words(stream, search_words)

                AppLogging().info("Tweepy stream has started")

            else:
                raise Exception("Tweepy stream failed to initiate")
        except Exception as e:
            AppLogging().exception(e)
