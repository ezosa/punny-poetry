# this script is originally from an assignment made for
# the NLP2019 course held in the University of Helsinki

from nltk.stem import WordNetLemmatizer
from nltk.corpus import cmudict
import editdistance
import random

lemmatizer = WordNetLemmatizer()  # used to lemmatize words.

with open('pungen/foods.txt', 'r') as f:
    food_pun_words = f.readlines()
with open('pungen/world-cities.txt', 'r') as f:
    cities_pun_words = f.readlines()
with open('pungen/adj.txt', 'r') as f:
    adj_pun_words = f.readlines()
    adj_pun_words = [w.strip() for w in adj_pun_words]

arpabet = cmudict.dict()


def make_punny(text, distance, theme='food'):
    all_pun_words = food_pun_words
    if theme == 'cities':
        all_pun_words = cities_pun_words

    pun_words = []

    for index, sent in enumerate(text):
        word = choose_first_eligible_word(sent)
        if word:
            pronounced_word = pronounce(word[0])
            if word[2] == 'NOUN':
                for k in food_pun_words:
                    k = k.replace('\n', '')
                    pronounced_food = check_pronounce(k)

                    if pronounced_food:
                        if editdistance.eval(pronounced_word, pronounced_food) < distance:
                            pun_words.append(k)
            else:
                for k in adj_pun_words:
                    k = k.replace('\n', '')
                    pronounced_food = check_pronounce(k)

                    if pronounced_food:
                        if editdistance.eval(pronounced_word, pronounced_food) < distance:
                            pun_words.append(k)
            if pun_words:
                text[index][word[1]][0] = random.choice(pun_words)
    return text


def check_pronounce(word):
    pronounced = pronounce(word)
    if pronounced:
        return pronounced
    else:
        return []


def pronounce(word):
    word = word.split()[-1]
    if word.lower() in arpabet:
        return arpabet[word.lower()][0]
    else:
        # make sure the word is lower-cased and exists in the dictionary
        return None


def choose_first_eligible_word(sent):
    eligible_words = []

    for i, (word, pos) in enumerate(sent):
        if pos in ('NOUN', 'ADJ'):
            eligible_words.append((word, i, pos))

    n = len(eligible_words)
    for i in range(n):
        pronounced_word = pronounce(eligible_words[i][0])
        if pronounced_word:
            return eligible_words[i]
    return None
