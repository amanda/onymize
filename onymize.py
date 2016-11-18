#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TODO:
    - change tokenizer to hold onto punctuation
    - put online

    - rewrite w rita for all in browser?
'''


from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk.tokenize import RegexpTokenizer


def find_syns(tokenized_text):
    '''(str) -> {adjective: [synonyms]}'''
    tagged = pos_tag(tokenized_text)
    synonyms = {}
    for tag in tagged:
        if tag[1] == 'JJ' and wn.synsets(tag[0]):
            lemmas = set([s.lemma_names()[0] for s in wn.synsets(tag[0])])
            if tag[0] in lemmas:
                lemmas.remove(tag[0])
            synonyms[tag[0]] = list(lemmas)
    return synonyms

def find_ants(tokenized_text):
    '''(str) -> {adjective: antonym}'''
    antonyms = {}
    tagged = pos_tag(tokenized_text)
    # TODO: clean up below?
    for tag in tagged:
        if tag[1] == 'JJ' and wn.synsets(tag[0]):
            for syn in wn.synsets(tag[0]):
                for lemma in syn.lemmas():
                    if lemma.antonyms():
                        antonyms[tag[0]] = lemma.antonyms()[0].name()
                        # TODO get all not just first one
    return antonyms


def choose_onymize(text, synonymize=True):
    '''
    (string, bool) -> string
    True = synonyms (default), False = antonyms
    iterates through text and writes an
    synonym antonym over each adjective
    ...it's slow for big texts
    '''
    tokenizer = RegexpTokenizer(r'\s+', gaps=True)
    tokenized = tokenizer.tokenize(text)
    if synonymize:
        syns = find_syns(tokenized)
        for word in tokenized:
            if word in syns:
                index = tokenized.index(word)
                tokenized.pop(index)
                tokenized.insert(index, syns[word])
        print 'synonymized!'
        return ' '.join(tokenized)
    ants = find_ants(tokenized)
    for word in tokenized:
        if word in ants:
            index = tokenized.index(word)
            tokenized.pop(index)
            tokenized.insert(index, ants[word])
    print 'antonymized!'
    return ' '.join(tokenized)
