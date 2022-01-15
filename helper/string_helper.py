def split_key_value(input_text, text_divider):
    obj = input_text.split(text_divider)
    return obj[0], obj[1]


def get_value_by_key(input_list, key):
    for i in range(len(input_list)):
        if input_list[i]["key"] == key:
            return input_list[i]["value"]


def remove_whitespace(str):
    return str.strip()


def replace_at_sign(obj):
    return obj.replace("@", "")


def remove_hashtag(obj):
    if obj.find("#") > 0:
        at_sign_start_index = obj.find("#")
        at_sign_end_index = obj.find(" ", at_sign_start_index)
        at_name = obj[at_sign_start_index:at_sign_end_index:]
        return obj.replace(at_name, "")
    return obj


def remove_user_at_name(obj):
    if obj.find("@") > 0:
        at_sign_start_index = obj.find("@")
        at_sign_end_index = obj.find(" ", at_sign_start_index)
        at_name = obj[at_sign_start_index:at_sign_end_index:]
        return obj.replace(at_name, "")
    return obj


def remove_url(obj):
    # at_sign_start_index = obj.index("@")
    # at_sign_end_index = obj.index(' ', at_sign_start_index)
    # at_name = obj[at_sign_start_index:at_sign_end_index:]
    return obj.replace("@", "")


def lowercase(obj):
    # at_sign_start_index = obj.index("@")
    # at_sign_end_index = obj.index(' ', at_sign_start_index)
    # at_name = obj[at_sign_start_index:at_sign_end_index:]
    return obj.lower()
