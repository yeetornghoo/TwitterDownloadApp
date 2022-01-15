import re
import string
import nltk
import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords

nltk.download("stopwords")
english_stop_words = set(stopwords.words("english"))

# ----------- REGEXP --------------------

REGEXP_hashtag = r"#[^\s]+"
REGEXP_special_char = r"(“|”|’|:)"
REGEXP_url = r"(?P<url>https?://[^\s]+)"
REGEXP_is_word = "[-A-Za-z]+'[Ss]+"
REGEXP_am_word = "[Ii]+'[Mm]+"
REGEXP_are_word = "[-A-Za-z]+'[ERer]+"
REGEXP_will_word = "[-A-Za-z]+'(LL|ll)"
REGEXP_have_word = "[-A-Za-z]+'(VE|ve)"
REGEXP_would_word = "[-A-Za-z]+'[Dd] "
REGEXP_at_user = "@[^\s]+"
REGEXP_didnt_word = r"[did|DID|Did]+'[not|t|nt]+"
REGEXP_dont_word = r"[do|DO|Do]+'[not|t|nt]+"


class CleanString:
    def simple_clean(self, input_str):
        input_str = process_single_line_str(input_str)
        input_str = process_lowercase_str(input_str)
        input_str = process_remove_url_str(input_str)
        input_str = process_extra_whitespace_str(input_str)
        return input_str

    def run(self, input_str):
        input_str = process_single_line_str(input_str)
        input_str = process_lowercase_str(input_str)
        input_str = process_hasgtag_str(input_str)
        input_str = process_special_char_str(input_str)
        input_str = process_remove_url_str(input_str)
        input_str = process_word_is_str(input_str)
        input_str = process_word_am_str(input_str)
        input_str = process_word_are_str(input_str)
        input_str = process_word_will_str(input_str)
        input_str = process_word_have_str(input_str)
        input_str = process_word_would_str(input_str)
        input_str = process_punctuation_str(input_str)
        # input_str = process_atusername_str(input_str)
        input_str = process_extra_whitespace_str(input_str)
        input_str = process_stop_words_str(input_str)
        input_str = process_remove_retweet_str(input_str)
        input_str = process_word_do_not_str(input_str)
        input_str = process_word_did_not_str(input_str)
        return input_str.strip()


class CleanDataframe:
    df = pd.DataFrame()

    def __init__(self, _df):
        self.df = _df

    def run_df(self, key_name):
        self.process_single_line_df(key_name)
        self.process_lowercase_df(key_name)
        self.process_hasgtag_df(key_name)
        self.process_special_char_df(key_name)
        self.process_remove_url_df(key_name)
        self.process_word_is_df(key_name)
        self.process_word_am_df(key_name)
        self.process_word_are_df(key_name)
        self.process_word_will_df(key_name)
        self.process_word_have_df(key_name)
        self.process_word_would_df(key_name)
        self.process_punctuation_df(key_name)
        self.process_atusername_df(key_name)
        self.process_extra_whitespace_df(key_name)
        self.process_stop_words_df(key_name)
        self.process_remove_retweet_df(key_name)
        self.process_word_do_not_df(key_name)
        self.process_word_did_not_df(key_name)
        return self.df

    def process_single_line_df(self, key_name):
        self.df[key_name] = self.df[key_name].apply(
            lambda x: process_single_line_str(str(x))
        )

    def process_lowercase_df(self, key_name):
        self.df[key_name] = self.df[key_name].apply(
            lambda x: process_lowercase_str(str(x))
        )

    def process_hasgtag_df(self, key_name):
        has_unchanged = True
        while has_unchanged:
            self.df[key_name] = self.df[key_name].apply(
                lambda x: process_hasgtag_str(str(x))
            )
            has_unchanged = has_unchanged_tweet(REGEXP_hashtag, self.df, key_name)

    def process_special_char_df(self, key_name):
        self.df[key_name] = self.df[key_name].apply(
            lambda x: process_special_char_str(str(x))
        )

    def process_remove_url_df(self, key_name):
        has_unchanged = True
        while has_unchanged:
            self.df[key_name] = self.df[key_name].apply(
                lambda x: process_remove_url_str(str(x))
            )
            has_unchanged = has_unchanged_tweet(REGEXP_url, self.df, key_name)

    def process_word_is_df(self, key_name):
        has_unchanged = True
        while has_unchanged:
            self.df[key_name] = self.df[key_name].apply(
                lambda x: process_word_is_str(str(x))
            )
            has_unchanged = has_unchanged_tweet(REGEXP_is_word, self.df, key_name)

    def process_word_am_df(self, key_name):
        has_unchanged = True
        while has_unchanged:
            self.df[key_name] = self.df[key_name].apply(
                lambda x: process_word_am_str(str(x))
            )
            has_unchanged = has_unchanged_tweet(REGEXP_am_word, self.df, key_name)

    def process_word_are_df(self, key_name):
        has_unchanged = True
        while has_unchanged:
            self.df[key_name] = self.df[key_name].apply(
                lambda x: process_word_are_str(str(x))
            )
            has_unchanged = has_unchanged_tweet(REGEXP_are_word, self.df, key_name)

    def process_word_will_df(self, key_name):
        has_unchanged = True
        reg_pattern = "[-A-Za-z]+'(LL|ll)"
        while has_unchanged:
            self.df[key_name] = self.df[key_name].apply(
                lambda x: process_word_will_str(str(x))
            )
            has_unchanged = has_unchanged_tweet(REGEXP_will_word, self.df, key_name)

    def process_word_have_df(self, key_name):
        has_unchanged = True
        reg_pattern = "[-A-Za-z]+'(VE|ve)"
        while has_unchanged:
            self.df[key_name] = self.df[key_name].apply(
                lambda x: process_word_have_str(str(x))
            )
            has_unchanged = has_unchanged_tweet(REGEXP_have_word, self.df, key_name)

    def process_word_would_df(self, key_name):
        has_unchanged = True
        reg_pattern = "[-A-Za-z]+'[Dd] "

        while has_unchanged:
            self.df[key_name] = self.df[key_name].apply(
                lambda x: process_word_would_str(str(x))
            )
            has_unchanged = has_unchanged_tweet(REGEXP_would_word, self.df, key_name)

    def process_punctuation_df(self, key_name):
        self.df[key_name] = self.df[key_name].apply(
            lambda x: process_punctuation_str(str(x))
        )

    def process_extra_whitespace_df(self, key_name):
        self.df[key_name] = self.df[key_name].apply(
            lambda x: process_extra_whitespace_str(str(x))
        )

    def process_atusername_df(self, key_name):
        has_unchanged = True
        while has_unchanged:
            self.df[key_name] = self.df[key_name].apply(
                lambda x: process_atusername_str(str(x))
            )
            has_unchanged = has_unchanged_tweet(REGEXP_at_user, self.df, key_name)

    def process_stop_words_df(self, key_name):
        self.df[key_name] = self.df[key_name].apply(
            lambda x: process_stop_words_str(str(x))
        )

    def process_remove_retweet_df(self, key_name):
        self.df[key_name] = self.df[key_name].apply(
            lambda x: process_remove_retweet_str(str(x))
        )

    def process_word_do_not_df(self, key_name):
        self.df[key_name] = self.df[key_name].apply(
            lambda x: process_word_do_not_str(str(x))
        )

    def process_word_did_not_df(self, key_name):
        self.df[key_name] = self.df[key_name].apply(
            lambda x: process_word_did_not_str(str(x))
        )


def process_single_line_str(sentence):
    return sentence.replace("\n", "")


def process_lowercase_str(sentence):
    return sentence.lower()


def process_hasgtag_str(sentence):
    return hasgtag_regexp(sentence, REGEXP_hashtag)


def process_special_char_str(sentence):
    sentence = sentence.replace("“", "")
    sentence = sentence.replace("”", "")
    sentence = sentence.replace(":", "")
    sentence = sentence.replace("’", "'")
    sentence = sentence.replace("(", "")
    sentence = sentence.replace(")", "")
    sentence = sentence.replace("]", "")
    sentence = sentence.replace("[", "")
    sentence = sentence.replace("…", "")
    sentence = sentence.replace("...", "")
    return sentence


def process_remove_url_str(sentence):
    search_result = re.search(REGEXP_url, sentence)
    if search_result is not None:
        sentence = sentence.replace(search_result[0], "")
    return sentence


def process_word_are_str(sentence):
    search_result = re.search(REGEXP_are_word, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("'", 1)
        replace_word = ("{} are".format(split_word[0])).lower()
        sentence = sentence.replace(word, replace_word)
    return sentence


def process_word_am_str(sentence):
    search_result = re.search(REGEXP_am_word, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("'", 1)
        replace_word = ("{} am".format(split_word[0])).lower()
        sentence = sentence.replace(word, replace_word)
    return sentence


def process_word_is_str(sentence):
    search_result = re.search(REGEXP_is_word, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("'", 1)
        replace_word = ("{} is".format(split_word[0])).lower()
        sentence = sentence.replace(word, replace_word.lower())
    return sentence


def process_word_will_str(sentence):
    search_result = re.search(REGEXP_will_word, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("'", 1)
        replace_word = ("{} will".format(split_word[0])).lower()
        sentence = sentence.replace(word, replace_word)
    return sentence


def process_word_have_str(sentence):
    search_result = re.search(REGEXP_have_word, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("'", 1)
        replace_word = ("{} ha{}".format(split_word[0], split_word[1])).lower()
        sentence = sentence.replace(word, replace_word)
    return sentence


def process_word_would_str(sentence):
    search_result = re.search(REGEXP_would_word, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("'", 1)
        replace_word = ("{} would ".format(split_word[0])).lower()
        sentence = sentence.replace(word, replace_word)
    return sentence


def process_punctuation_str(text):
    return text.translate(str.maketrans("", "", string.punctuation))


def process_atusername_str(sentence):
    search_result = re.search(REGEXP_at_user, sentence)
    if search_result is not None:
        word = search_result[0]
        sentence = sentence.replace(word, "")
    return sentence


def process_extra_whitespace_str(sentence):
    sentence = sentence.replace("    ", " ")
    sentence = sentence.replace("   ", " ")
    sentence = sentence.replace("  ", " ")
    sentence = sentence.replace("\n", " ").replace("\r", "")
    return sentence


def process_stop_words_str(sentence):
    word_tokens = word_tokenize(sentence)
    filtered_sentence = [w for w in word_tokens if not w.lower() in english_stop_words]
    return " ".join(filtered_sentence)


def process_remove_retweet_str(sentence):
    sentence = sentence.replace("rt ", " ")
    sentence = sentence.replace("RT ", " ")
    return sentence


def process_word_do_not_str(sentence):
    sentence = sentence.replace("didt ", "did not")
    sentence = sentence.replace("did't ", "did not")
    sentence = sentence.replace("did'nt ", "did not")
    return sentence


def process_word_did_not_str(sentence):
    sentence = sentence.replace("don't ", "did not")
    sentence = sentence.replace("dont ", "did not")
    return sentence


# ----------------------------------------
# FUNCTION
# ----------------------------------------


def split_hashtag(word):
    split_reg_pattern = "[A-Z][^A-Z]*"
    if word != word.upper():
        split_word = re.findall(split_reg_pattern, word)
        if len(split_word) > 1:
            word = " ".join(map(str, split_word))
    return word


def hasgtag_regexp(sentence, reg_pattern):
    search_result = re.search(reg_pattern, sentence)
    if search_result is not None:
        word = search_result[0]
        to_word = split_hashtag(word.replace("#", ""))
        sentence = sentence.replace(word, to_word)
    return sentence


def has_unchanged_tweet(reg_pattern, df, key_name):
    for index, row in df.iterrows():
        search_result = re.search(reg_pattern, row[key_name])
        if search_result is not None:
            return True
    return False
