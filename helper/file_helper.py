import shutil
import os
#import pandas as pd
from helper import datetime_helper
from helper import config_helper


def get_line_from_file(file_path):
    objs = []
    try:
        with open(file_path) as fp:
            line = fp.readline()
            while line:
                objs.append(line.strip().lower())
                line = fp.readline()
    finally:
        fp.close()

    return objs


def get_items_from_file(file_path):
    dict_items = {}
    try:
        with open(file_path) as fp:
            lines = fp.readlines()
            for line in lines:
                items = line.split("=")
                if items is not None and len(items) >= 2:
                    config_key = items[0].strip()
                    config_value = items[1].strip()
                    dict_item = {config_key:config_value}
                    dict_items.update(dict_item)
    except ValueError:
        print("Error")
    finally:
        return dict_items


def create_tweeet_stream_file(file_name):
    output_file_name = "{}_{}.txt".format(file_name, datetime_helper.now_file_name())
    f = open("topic/" + output_file_name, "w+")
    return output_file_name, f


def initiate_file(topic_name):
    file_path = config_helper.get_twitter_raw_file(topic_name)
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
        f = open(file_path, "w+")
        return f
    finally:
        print("initiated!")


def backup_raw_file(file_path, topic_name):
    log_file_path = config_helper.get_twitter_raw_file_log(topic_name)
    print("copied from " + file_path + " to " + log_file_path)
    shutil.copy(file_path, log_file_path)


def is_raw_file_size_exceed(file_path):
    max_file_size = int(config_helper.get_twitter_raw_file_size())
    current_file_size = int(file_size(file_path))
    if current_file_size > max_file_size:
        return True
    else:
        return False


def write_to_file(topic_name, f, data):
    # GET FILE PATH
    # file_path = AppConfigHelper.get_twitter_raw_file(topic_name)
    f.write(data)
    """
    # CHECK CURRENT FILE
    if is_raw_file_size_exceed(file_path):
        backup_raw_file(file_path, topic_name)
        f.close()
    """


def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return file_info.st_size


# def read_json_text_file_to_df(file_path):
#     df = pd.DataFrame()
#     file = open(file_path, "r", encoding="utf8")
#     lines = file.readlines()
#
#     for line in lines:
#         json_str = line.strip()
#         json_obj = json.loads(json_str)
#         df = df.append(json_obj, ignore_index=True)
#
#     return df
