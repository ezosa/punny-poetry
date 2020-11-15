from nltk import sent_tokenize, pos_tag
import json
import wikipediaapi
import argparse

parser = argparse.ArgumentParser(description='Limerick Generator')
parser.add_argument('--theme', type=str, default='Amsterdam', help='Theme of the limerick')
args = parser.parse_args()

# choose random limerick template
templates = 


