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

with open('foods.txt', 'r') as f:
    food_pun_words = f.readlines()
with open('world-cities.txt', 'r') as f:
    cities_pun_words = f.readlines()

arpabet = cmudict.dict()


def pronounce(word):
    if word.lower() in arpabet:
        return arpabet[word.lower()][0]
    else:
        return None  # make sure the word is lowercased and
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


def make_punny(text, distance, theme):
    if theme == 'food':
        all_pun_words = food_pun_words
    elif theme == 'cities':
        all_pun_words = cities_pun_words
    processed_text = process_text(text)
    pun_words = []
    pun_sentence = ""
    pun_sentences = []

    for index, sent in enumerate(processed_text):
        word = choose_random_word(sent)
        pronounced_word = pronounce(word[0])
        # print(word)
        for k in all_pun_words:
            k = k.replace('\n', '')
            pronounced_food = check_pronounce(k)

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
    print(make_punny("Jurassic Park", 2, "food"))
    print(make_punny("Jurassic Park", 3, "cities"))
    print(make_punny("Life of Pi", 2, "food"))
    print(make_punny("Life of Pi", 3, "cities"))
    print(make_punny("Gone with the wind", 2, "food"))
    print(make_punny("Gone with the wind", 3, "cities"))
    print(make_punny("The Lord of the Rings", 3, "food"))
    print(make_punny("The Lord of the Rings", 4, "cities"))
    line = ' '
    while line != '':
        line = input("try your line (empty line to exit): ")
        if line != '':
            print(make_punny(line,3))
            print(make_punny(line,3))
            print(make_punny(line,4))


if __name__ == "__main__":
    main()
