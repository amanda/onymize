'''switches adjectives in a text with their synonyms,
or antonyms'''

from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag


def synonymize(text):
    '''(str) -> {adjective: [synonyms]}'''
    tagged = pos_tag(word_tokenize(text))
    for t in tagged:
        if t[1] == 'JJ' and wn.synsets(t[0]):
            lemmas = set([s.lemma_names()[0] for s in wn.synsets(t[0])])
            lemmas.remove(t[0])
            return {t[0]: list(lemmas)}

def antonymize(text):
    '''(str) -> {adjective: [antonyms]}'''
    pass


def replace_words(textfile, onymize_desire):
    '''iterates through text in a file, writes
    new synonym or antonym over each adjective'''
    pass
    pass
