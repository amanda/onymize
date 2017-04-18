'''
analyze text sentiment
if postive, antonymize
'''

from textblob import TextBlob
from onymize import onymize

def get_setiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def make_it_sad(text, sadness_cutoff=1):
    sentiment = get_setiment(text):
    if sentiment < sadness_cutoff:
        return onymize(text, False)
