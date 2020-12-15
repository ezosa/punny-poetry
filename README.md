# Punny Poetry
Generate themed punny limericks!

## System Requirements

- Python 3.6 or higher

### Depenedencies
```
pip install Wikipedia-API
pip install spacy
pip install editdistance
```
You also need to download the English model for spaCy and NLTK's CMUDict:
```
python -m spacy download en
python -m nltk.downloader cmudict
```

## Starting point

To generate a limerick about Amsterdam:
```
python main.py --theme Amsterdam 
```

You can try other themes too!
```
python main.py --theme Budapest
python main.py --theme Christmas
```

## Resources
- List of cities: https://datahub.io/core/world-cities, http://www.geonames.org/, https://github.com/lexman, https://okfn.org/
