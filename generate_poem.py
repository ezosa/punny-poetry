from nltk import sent_tokenize, pos_tag
import json
import wikipediaapi
import random
import spacy
import editdistance
from nltk.corpus import cmudict
import string

exclude = list(string.punctuation)
arpabet = cmudict.dict()
nlp = spacy.load('en')


def get_wiki_text(theme):
    wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    wiki_text = wiki.page(theme).text
    return wiki_text


# get entities from text
def get_entities_from_text(wiki_text):
    text = nlp(wiki_text)
    persons = []
    places = []
    for ent in text.ents:
        if ent.label_ == 'PERSON':
            if len(ent) > 1:
                persons.append(ent.text.strip())
        elif ent.label_ == 'GPE':
            if len(ent) > 1:
                places.append(ent.text.strip())
    persons = list(set(persons))
    places = list(set(places))
    return persons, places


# pick random limerick template
def pick_random_template():
    templates = json.load(open("templates/templates_universal.json", "r"))
    random_num = random.choice(range(len(templates)))
    template = templates[str(random_num)]
    invalid_temp = True
    while invalid_temp is True:
        line_lengths = [len(line) for line in template]
        if 0 not in line_lengths:
            invalid_temp = False
        else:
            random_num = random.choice(range(len(templates)))
            template = templates[str(random_num)]
    return template


# substitute words in template
def new_limerick_from_template(template, persons, places):
    new_limerick = []
    for l, line in enumerate(template):
        new_line = []
        #line_pos = "|".join([tok[1] for tok in line])
        for t, tok in enumerate(line):
            pos = tok[1]
            value = tok[0]
            if pos in (['DET', 'VERB', 'ADP', 'PRON']):
                new_line.append([value, pos])
            else:
                if pos == 'NOUN':
                    # select a random entity from list
                    prev_pos = line[t-1][1]
                    if prev_pos == 'ADP':
                        random_ent = random.choice(places)
                    else:
                        random_ent = random.choice(persons)
                    if prev_pos != 'NOUN':
                        if value[0].isupper() == True:
                            new_line.append([random_ent, pos])
                        else:
                            new_line.append([value, pos])
        #new_line = ' '.join(new_line)
        #print(new_line)
        new_limerick.append(new_line)
    return new_limerick


# fix rhyme scheme
def pronounce(word):
    return arpabet[word.lower()][0] if word.lower() in arpabet else None  # make sure the word is lowercased and
    # exists in the dictionary


def pronounce_dist(word1, word2):
    pron_word1 = pronounce(word1)
    pron_word2 = pronounce(word2)
    if pron_word1 is not None and pron_word2 is not None:
        dist = editdistance.eval(pron_word1, pron_word2)
    else:
        dist = 10
    return dist


def clean_word(word):
    print("clean word:", word)
    # remove punctuations and digits
    word = ''.join([c if c not in exclude else ' ' for c in word ])
    word = ''.join([c for c in word if not c.isdigit()])
    # if word is actually a noun phrase, just return last token
    tokens = word.split()
    if len(tokens) > 0:
        word = tokens[-1]
    print("new word:", word)
    return word


def generate_rhymes(word1, word2, pos2, text):
    dist = pronounce_dist(word1, word2)
    if dist >=3:
        for token in text:
            if token.pos_ == pos2:
                word2 = token.text
                word2 = clean_word(word2)
                dist = pronounce_dist(word1, word2)
                if dist <= 3:
                    break
    return word2


def fix_rhyme_scheme(new_limerick, wiki_text):
    text = nlp(wiki_text)
    # fix rhyme scheme for lines 1 and 2
    word1 = new_limerick[0][-1][0]
    word2 = new_limerick[1][-1][0]
    word1 = clean_word(word1)
    word2 = clean_word(word2)
    pos2 = new_limerick[1][-1][1]
    print("Word1:", word1)
    print("Word2:", word2)
    print("POS2:", pos2)
    word2 = generate_rhymes(word1, word2, pos2, text)
    print("New Word2:", word2)
    new_limerick[1][-1][0] = word2
    # fix rhyme scheme for lines 3 and 4
    word3 = new_limerick[2][-1][0]
    word4 = new_limerick[3][-1][0]
    word3 = clean_word(word3)
    word4 = clean_word(word4)
    pos4 = new_limerick[3][-1][1]
    print("Word3:", word3)
    print("Word4:", word4)
    print("POS4:", pos2)
    word4 = generate_rhymes(word3, word4, pos4, text)
    print("New Word4:", word4)
    new_limerick[3][-1][0] = word4
    # fix rhyme scheme for line 5
    new_limerick[4][-1][0] = word1
    return new_limerick



