# helpfunctions


import nltk
from HanTa import HanoverTagger as ht

tagger = ht.HanoverTagger('morphmodel_ger.pgz')


def get_nouns (string):
    nouns = [] 
    sentences_tok = [nltk.tokenize.word_tokenize(string)]
    for sent in sentences_tok:
        tags = tagger.tag_sent(sent) 
        nouns_from_sent = [lemma for (word,lemma,pos) in tags if pos == "NN" or pos == "NE"]
    return nouns_from_sent

def get_verbs (string):
    nouns = [] 
    sentences_tok = [nltk.tokenize.word_tokenize(string)]
    for sent in sentences_tok:
        tags = tagger.tag_sent(sent) 
        nouns_from_sent = [lemma for (word,lemma,pos) in tags if pos == "VAFIN" or pos == "VVPP" or pos =="VVFIN"]
    return nouns_from_sent

def get_adjectives (string):
    nouns = [] 
    sentences_tok = [nltk.tokenize.word_tokenize(string)]
    for sent in sentences_tok:
        tags = tagger.tag_sent(sent) 
        nouns_from_sent = [lemma for (word,lemma,pos) in tags if pos == "ADJA" or pos == "ADJ"]
    return nouns_from_sent
# helperfile

def get_func (df, func):
    df['nouns'] = df['-5'].apply(func)
    return df



