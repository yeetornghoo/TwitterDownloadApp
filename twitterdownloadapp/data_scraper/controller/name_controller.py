import re
import string
from wordcloud import WordCloud
import pandas as pd
import nltk

nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

# nlp = en_core_web_sm.load()


class NameController:

    df = pd.DataFrame()
    long_string = ""

    def __init__(self, _df, _key_name):
        self.long_string = ",".join(list(_df[_key_name].values))

    def run(self):
        persons = get_name_entity(self.long_string)
        print(persons)


def generate_wordcloud(long_string):
    wordcloud = WordCloud(
        background_color="white",
        max_words=5000,
        contour_width=3,
        contour_color="steelblue",
    )
    wordcloud.generate(long_string)
    wordcloud.to_image()


def get_name_entity(doc):
    print("----get_name_entity----")
    print(doc)
    # print([(X, X.ent_iob_, X.ent_type_) for X in doc])


"""
def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
"""
"""
    for subtree in sentt:

        print("'{}' => '{}'".format(subtree, len(subtree)))

        if len(subtree) <= 1:
            continue

        if subtree[1] == "PERSON":
            person.append(subtree)

    print(person)
"""
"""
    for subtree in sentt.subtrees(filter=lambda t: t.node == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list)
"""
