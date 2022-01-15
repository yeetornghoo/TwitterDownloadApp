__author__ = "CH"

from twitterdownloadapp.data_scraper import ProcessTweepy

if __name__ == "__main__":
    try:
        ProcessTweepy().run()
    finally:
        print("Downloading...")
