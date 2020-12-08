import argparse
from generate_poem import get_wiki_text, get_entities_from_text, pick_random_template, new_limerick_from_template, fix_rhyme_scheme

# parser = argparse.ArgumentParser(description='Limerick Generator')
# parser.add_argument('--theme', type=str, default='Amsterdam', help='Theme of the limerick')
# args = parser.parse_args()
# theme = args.theme.lower()
#
# print("="*10, "Welcome to our Punny Limerick Generator!", "="*10)
# print("Your chosen theme:", theme)

theme = 'Amsterdam'

# get Wikipage page and extract entities
wiki_text = get_wiki_text(theme)
persons, places = get_entities_from_text(wiki_text)

# select random template
template = pick_random_template()

# generate new limerick from template
new_limerick = new_limerick_from_template(template, persons, places)
new_limerick2 = fix_rhyme_scheme(new_limerick, wiki_text)

# print limerick
print("New limerick:")
for line in new_limerick2:
    line_str = " ".join([tok[0] for tok in line])
    print(line_str)
