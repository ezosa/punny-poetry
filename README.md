# Punny Poetry
Generate pun-filled limericks about anything!

## System Requirements

- Python 3.7 or higher

### Dependencies
```
pip install Wikipedia-API
pip install spacy
pip install editdistance
pip install nltk
```
You also need to download the English model for spaCy and NLTK's CMUDict:
```
python -m spacy download en
python -m nltk.downloader cmudict
```

## Starting point

To generate a limerick about Amsterdam:
```
python main.py --topic Amsterdam 
```

You can try other themes too!
```
python main.py --topic London
python main.py --topic Christmas
```

## Resources
- List of cities: https://datahub.io/core/world-cities, http://www.geonames.org/, https://github.com/lexman, https://okfn.org/
