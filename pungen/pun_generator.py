# this script is originally from an assignment made for
# the NLP2019 course held in the University of Helsinki

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import cmudict
import requests
import xmltodict
import pickle
import os
import editdistance
import random

lemmatizer = WordNetLemmatizer()  # used to lemmatize words.


def food_words(file_path='./food_words.pkl'):
    if os.path.isfile(file_path):  # load stored results
        with open(file_path, 'rb') as f:
            return pickle.load(f)

    url = 'http://ngrams.ucd.ie/therex3/common-nouns/head.action?head=food&ref=apple&xml=true'
    response = requests.get(url)
    result = xmltodict.parse(response.content)
    _root_content = result['HeadData']
    result_dict = dict(map(lambda r: tuple([r['#text'].replace('_', ' ').strip(), int(r['@weight'])]), _root_content['Members']['Member']))

    with open(file_path, 'wb') as f:  # store the results locally (as a cache)
        pickle.dump(result_dict, f, pickle.HIGHEST_PROTOCOL)
    return result_dict


arpabet = cmudict.dict()


def pronounce(word):
    return arpabet[word.lower()][0] if word.lower() in arpabet else None  # make sure the word is lowercased and
    # exists in the dictionary


def process_text(text):
    processed_sentences = []

    sentences = sent_tokenize(text)
    for sent in sentences:
        temp_sent = []
        sent = word_tokenize(sent)
        sent = pos_tag(sent)
        for word, pos in sent:
            temp_sent.append((word, lemmatizer.lemmatize(word), pos))
        processed_sentences.append(temp_sent)

    return processed_sentences


def make_punny(text, distance):
    foods = food_words()
    processed_text = process_text(text)
    pun_words = []
    pun_sentence = ""
    pun_sentences = []

    for index, sent in enumerate(processed_text):
        word = choose_random_word(sent)
        # print(word)
        for k, v in foods.items():
            pronounced_food = check_pronounce(k)
            pronounced_word = pronounce(word[0])
            if pronounced_food and pronounced_word:
                if editdistance.eval(pronounced_word, pronounced_food) < distance:
                    pun_words.append(k)
                    # print(pun_words)
                    processed_text[index][word[1]] = random.choice(pun_words)
        for w in sent:
            if type(w) == tuple:
                pun_sentence += w[0] + " "
            else:
                pun_sentence += w + " "
        pun_sentences.append(pun_sentence)

    return pun_sentences[0]


def check_pronounce(word):
    pronounced = pronounce(word)
    if pronounced:
        return pronounced
    else:
        return []


def choose_random_word(sent):
    eligible_words = []
    index = 0

    for word, lemma, pos in sent:
        if pos in ('NN', 'NNS', 'NNP', 'NNPS', 'VBP', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'):
            eligible_words.append((word, index))
        index += 1

    # print(eligible_words)
    return random.choice(eligible_words)


def main():
    print("This script can make food puns like examples below (it might take few seconds):")
    print(make_punny("Jurassic Park", 2))
    print(make_punny("Jurassic Park", 3))
    print(make_punny("Life of Pi", 2))
    print(make_punny("Life of Pi", 3))
    print(make_punny("gone with the wind", 2))
    print(make_punny("gone with the wind", 3))
    print(make_punny("The Lord of the Rings", 3))
    print(make_punny("The Lord of the Rings", 4))
    line = ' '
    while line != '':
        line = input("try your line (empty line to exit): ")
        if line != '':
            print(make_punny(line,3))
            print(make_punny(line,3))
            print(make_punny(line,4))


if __name__ == "__main__":
    main()
