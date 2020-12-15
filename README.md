# Punny Poetry
Computational Creativity course (Fall 2020) at the University of Helsinki

Generate themed punny limericks!

## Dependencies
- Python 3.6 or higher

### Required packages
```
pip install Wikipedia-API
pip install spacy
pip install editdistance
```
You also need to download the English model for spaCy:
```
python -m spacy download en
```
And download NLTK's CMUDict:
```
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
