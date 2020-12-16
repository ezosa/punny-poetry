import argparse
from generate_poem import get_wiki_text, get_entities_from_text, pick_random_template, new_limerick_from_template, fix_rhyme_scheme
from pungen.pun_generator import make_punny

parser = argparse.ArgumentParser(description='Limerick Generator')
parser.add_argument('--topic', type=str, default='Amsterdam', help='Topic of the limerick')
args = parser.parse_args()
topic = args.topic.lower()

topic = 'London'
pun_theme = 'food'

print("="*10, "Welcome to our Punny Limerick Generator!", "="*10)
print("Your chosen topic:", topic)

# get Wikipage page and extract entities
wiki_text = get_wiki_text(topic)
persons, places = get_entities_from_text(wiki_text)

# select random template
template = pick_random_template()

# generate new limerick from template
new_limerick = new_limerick_from_template(template, persons, places)
new_limerick2 = fix_rhyme_scheme(new_limerick, wiki_text)
new_limerick3 = make_punny(new_limerick2, 2, pun_theme)

# print limerick
print("*"*5, "Here's your new limerick!", "*"*5)
for line in new_limerick3:
    line_str = " ".join([tok[0] for tok in line])
    print(line_str)
