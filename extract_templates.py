from nltk import word_tokenize, pos_tag
import json
import spacy
nlp = spacy.load('en')


def extract_limericks_from_text(text):
    limericks = []
    cur_index = start_index
    while cur_index < len(text):
        # found start of limerick
        if len(text[cur_index]) > 10:
            limerick = text[cur_index:cur_index+len_lines]
            limericks.append(limerick)
            cur_index += len_lines
        # current line is empty, move to next line
        else:
            cur_index += 1
    return limericks


def tag_limericks(limericks, tagset=None):
    tagged_limericks = []
    for limerick in limericks:
        tagged_lines = []
        for line in limerick:
            if tagset is None:
                tags = pos_tag(line.strip().split())
            else:
                tags = pos_tag(line.strip().split(), tagset=tagset)
            tagged_lines.append(tags)
        tagged_limericks.append(tagged_lines)
    return tagged_limericks


def tag_limericks_spacy(limericks):
    tagged_limericks = []
    for limerick in limericks:
        tagged_lines = []
        for line in limerick:
            tagged_line = []
            line = line.strip()
            #print("Line:", line)
            line_tagged = nlp(line)
            for token in line_tagged:
                tok = []
                tok.append(token.text)
                tok.append(token.pos_)
                tagged_line.append(tok)
            for chunk in line_tagged.noun_chunks:
                tagged_line.append(chunk.text)
            tagged_lines.append(tagged_line)
        tagged_limericks.append(tagged_lines)
    return tagged_limericks


def assemble_templates(tagged_limericks):
    templates = {}
    for i, tagged in enumerate(tagged_limericks):
        #for i, line in enumerate(tagged):
        templates[i] = tagged
    return templates


text = open('data/Book-of-Nonsense-Lear.txt', 'r', encoding='utf-8').readlines()
start_index = 74
len_lines = 5
tagset = 'universal'
nlp = spacy.load('en')

limericks_text = extract_limericks_from_text(text)
#tagged_limericks = tag_limericks(limericks_text, tagset=tagset)
tagged_limericks = tag_limericks_spacy(limericks_text)
templates = assemble_templates(tagged_limericks)
# write templates to file
json_file = open("templates/templates_" + tagset + ".json", 'w')
json.dump(templates, json_file)