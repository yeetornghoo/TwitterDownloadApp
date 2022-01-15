__author__ = "CH"

from data_scraper import search_location_list


def get_twitter_location_regexp_filter():
    locations_str = ""
    for location in search_location_list:
        item = " {} ".format(location)
        if len(locations_str.strip()) <= 0:
            locations_str = "{}".format(item)
        else:
            locations_str = "{}|{}".format(locations_str, item)
    return "(?i)({})".format(locations_str)
