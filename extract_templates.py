from nltk import word_tokenize, pos_tag
import json


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


def assemble_templates(tagged_limericks):
    templates = {}
    for tagged in tagged_limericks:
        for i, line in enumerate(tagged):
            if i not in templates:
                templates[i] = []
            tags = [tok[1] for tok in line]
            tags_str = " | ".join(tags)
            if len(tags_str) > 0 and tags_str not in templates[i]:
                templates[i].append(tags_str)
    return templates

text = open('data/Book-of-Nonsense-Lear.txt', 'r', encoding='utf-8').readlines()
start_index = 74
len_lines = 5
tagset = 'universal'

limericks_text = extract_limericks_from_text(text)
tagged_limericks = tag_limericks(limericks_text, tagset=tagset)
templates = assemble_templates(tagged_limericks)
# write templates to file
json_file = open("templates_" + tagset + ".json", 'w')
json.dump(templates, json_file)