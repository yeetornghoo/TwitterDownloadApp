__author__ = "CH"

from data_scraper.controller.tweepy.process import ProcessTweepy

if __name__ == "__main__":
    try:
        ProcessTweepy().run()
    finally:
        print("Downloading...")
