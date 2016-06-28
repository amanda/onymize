'''switches adjectives in a text with their synonyms,
or antonyms'''

from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag


def find_syns(tokenized_text):
    '''(str) -> {adjective: [synonyms]}'''
    tagged = pos_tag(tokenized_text)
    synonyms = {}
    for t in tagged:
        if t[1] == 'JJ' and wn.synsets(t[0]):
            lemmas = set([s.lemma_names()[0] for s in wn.synsets(t[0])])
            lemmas.remove(t[0])
            synonyms[t[0]] = list(lemmas)
    return synonyms

def find_ants(tokenized_text):
    '''(str) -> {adjective: [antonyms]}'''
    antonyms = {}
    tagged = pos_tag(tokenized_text)
    # TODO: clean up below?
    for t in tagged:
        if t[1] == 'JJ' and wn.synsets(t[0]):
            for syn in wn.synsets(t[0]):
                for l in syn.lemmas():
                    if l.antonyms():
                        antonyms[t[0]] = l.antonyms()[0].name() # TODO check if only 1
    return antonyms


def antonymize(text):
    '''iterates through text and writes an
    antonym over each adjective...it's slow'''
    tokenized = word_tokenize(text)
    ants = find_ants(tokenized)
    for w in tokenized:
        pass
