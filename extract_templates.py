from nltk import word_tokenize, pos_tag

text = open('data/Book-of-Nonsense-Lear.txt', 'r', encoding='utf-8').readlines()
start_index = 74
len_lines = 5


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


def tag_limericks(limericks):
    tagged_limericks = []
    for limerick in limericks:
        tagged_lines = []
        for line in limerick:
            tags = pos_tag(line.split())
            tagged_lines.append(tags)
        tagged_limericks.append(tagged_lines)
    return tagged_limericks


def assemble_templates(tagged_limericks):
    templates = {}
        
    return templates


limericks_text = extract_limericks_from_text(text)
limericks_tags = tag_limericks(limericks_text)


