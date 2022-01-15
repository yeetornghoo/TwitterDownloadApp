from helper import datetime_helper
from datetime import datetime

app_config_file_path = "app.tweet_config"


def get_current_datetime_for_filename():
    return datetime.today().strftime("%Y%m%d-%H%M")


def get_value_by_key(line):
    start_index = line.index("=") + 1
    return line[start_index:].strip()


def get_app_config_by_key(key):
    with open(app_config_file_path, "r") as read_obj:
        for line in read_obj:
            if key in line:
                return get_value_by_key(line)
    return None


def get_twitter_raw_file(file_name):
    folder_path = get_app_config_by_key("twitter_topic_folder")
    file_path = "{}raw_{}_{}.txt".format(
        folder_path, file_name, get_current_datetime_for_filename()
    )
    return file_path


def get_twitter_raw_file_log(file_name):
    folder_path = get_app_config_by_key("twitter_topic_folder")
    now_string = datetime_helper.now_file_name()
    file_path = "{}log/raw_{}_{}.txt".format(folder_path, file_name, now_string)
    return file_path


def get_twitter_raw_file_size():
    key = "twitter_topic_raw_file_size"
    return get_app_config_by_key(key)


# a = AppConfigHelper.get_twitter_folder()
# print("a:" + a)
