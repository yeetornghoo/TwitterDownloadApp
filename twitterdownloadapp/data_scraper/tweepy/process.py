__author__ = "CH"

import tweepy as tweepy
from twitterdownloadapp.data_scraper import api, search_words

"""
from twitterdownloadapp.data_scraper import TweepyStream
location_regex = '(?i)(malaysia|kl|selangor|johor|perlis|kedah|sabah|sarawak' \
                 '|kelantan|penang|perak|pahang|terrengganu|malacca' \
                 '|negeri sembilan|kuala lumpur)'

def is_desired_location(data):
    return re.search(location_regex, str(data).upper())


def process_stream_tweet(data, f):
    new_input_dict = {}

    if is_desired_location(data):

        json_input = json.loads(data)

        new_input_dict["tweet.created_at"] = json_input["created_at"]
        new_input_dict["tweet.id"] = json_input["id"]
        new_input_dict["tweet.text"] = json_input["text"]
        new_input_dict["user.id"] = json_input["user"]["id"]
        new_input_dict["user.name"] = json_input["user"]["name"]
        new_input_dict["user.screen_name"] = json_input["user"]["screen_name"]
        new_input_dict["user.location"] = json_input["user"]["location"]

        if json_input["place"] is not None:
            new_input_dict["tweet.place"] = json_input["place"]["id"]
            new_input_dict["tweet.place.full_name"] = json_input["place"]["full_name"]
            new_input_dict["tweet.place.country_code"] = json_input["place"]["country_code"]
        else:
            new_input_dict["tweet.place"] = None
            new_input_dict["tweet.place.full_name"] = None
            new_input_dict["tweet.place.country_code"] = None

        new_input_dict["tweet.retweeted"] = json_input["retweeted"]
        new_input_dict["tweet.lang"] = json_input["lang"]

        print(new_input_dict)
        json.dump(new_input_dict, f)
        f.write('\n')
"""


class ProcessTweepy:

    search_words = ""

    def __init__(self):
        print("----")

    def run(self):

        TweepyCursor().run()
        # TweepyStream().run()
        # TweepyStream().users()


class TweepyCursor:

    BATCH_COUNT = 5

    def save_tweets(self, tweets):
        for tweet in tweets:
            print(tweet)
            # self.conn.insert_raw_twitter(tweet)

    def download_save(self, locations):
        tweets = tweepy.Cursor(
            api.search_tweets, q=search_words, geocode=locations
        ).items(self.BATCH_COUNT)
        self.save_tweets(tweets)

    def process_west_malaysia(self):
        locations = "4.7259518408729,101.8085617846325,500km"
        self.download_save(locations)

    def run(self):
        self.process_west_malaysia()
