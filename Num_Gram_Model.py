"""
Assignment No 3
Name - Abhishek Kusalkar
Batch - B2
Roll No - 35
Assignment Title : Generating The N Gram Model using NLTK

"""

from nltk import ngrams
from nltk.util import ngrams

#unigram model
n = 1
sentence = 'While unigram model sentences will only exclude the UNK token, models will also exclude all other words already in the sentence.NTK provides another function everygrams that converts a sentence into unigram, bigram, trigram, and so on till the ngrams, where n is the length of the sentence. In short, this function generates ngrams for all possible values of n.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)

    
#bigram model
n = 2
sentence = 'While unigram model sentences will only exclude the UNK token, models will also exclude all other words already in the sentence.NTK provides another function everygrams that converts a sentence into unigram, bigram, trigram, and so on till the ngrams, where n is the length of the sentence. In short, this function generates ngrams for all possible values of n.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)


#trigram model
n = 3
sentence = 'While unigram model sentences will only exclude the UNK token, models will also exclude all other words already in the sentence.NTK provides another function everygrams that converts a sentence into unigram, bigram, trigram, and so on till the ngrams, where n is the length of the sentence. In short, this function generates ngrams for all possible values of n.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)


#using text file input

from nltk import ngrams
file = open("/home/exam/Awesome-NLP/Num.txt")
for i in file.readlines():
    cumulative = i
    sentences = i.split(".")
    counter = 0
    for sentence in sentences:
        print("For sentence", counter + 1, ", trigrams are: ")
        trigrams = ngrams(sentence.split(" "), 3)
        for grams in trigrams:
            print(grams)
        counter += 1
        print()

# OUTPUT -
"""

('While',)
('unigram',)
('model',)
('sentences',)
('will',)
('only',)
('exclude',)
('the',)
('UNK',)
('token,',)
('models',)
('will',)
('also',)
('exclude',)
('all',)
('other',)
('words',)
('already',)
('in',)
('the',)
('sentence.NTK',)
('provides',)
('another',)
('function',)
('everygrams',)
('that',)
('converts',)
('a',)
('sentence',)
('into',)
('unigram,',)
('bigram,',)
('trigram,',)
('and',)
('so',)
('on',)
('till',)
('the',)
('ngrams,',)
('where',)
('n',)
('is',)
('the',)
('length',)
('of',)
('the',)
('sentence.',)
('In',)
('short,',)
('this',)
('function',)
('generates',)
('ngrams',)
('for',)
('all',)
('possible',)
('values',)
('of',)
('n.',)
('While', 'unigram')
('unigram', 'model')
('model', 'sentences')
('sentences', 'will')
('will', 'only')
('only', 'exclude')
('exclude', 'the')
('the', 'UNK')
('UNK', 'token,')
('token,', 'models')
('models', 'will')
('will', 'also')
('also', 'exclude')
('exclude', 'all')
('all', 'other')
('other', 'words')
('words', 'already')
('already', 'in')
('in', 'the')
('the', 'sentence.NTK')
('sentence.NTK', 'provides')
('provides', 'another')
('another', 'function')
('function', 'everygrams')
('everygrams', 'that')
('that', 'converts')
('converts', 'a')
('a', 'sentence')
('sentence', 'into')
('into', 'unigram,')
('unigram,', 'bigram,')
('bigram,', 'trigram,')
('trigram,', 'and')
('and', 'so')
('so', 'on')
('on', 'till')
('till', 'the')
('the', 'ngrams,')
('ngrams,', 'where')
('where', 'n')
('n', 'is')
('is', 'the')
('the', 'length')
('length', 'of')
('of', 'the')
('the', 'sentence.')
('sentence.', 'In')
('In', 'short,')
('short,', 'this')
('this', 'function')
('function', 'generates')
('generates', 'ngrams')
('ngrams', 'for')
('for', 'all')
('all', 'possible')
('possible', 'values')
('values', 'of')
('of', 'n.')
('While', 'unigram', 'model')
('unigram', 'model', 'sentences')
('model', 'sentences', 'will')
('sentences', 'will', 'only')
('will', 'only', 'exclude')
('only', 'exclude', 'the')
('exclude', 'the', 'UNK')
('the', 'UNK', 'token,')
('UNK', 'token,', 'models')
('token,', 'models', 'will')
('models', 'will', 'also')
('will', 'also', 'exclude')
('also', 'exclude', 'all')
('exclude', 'all', 'other')
('all', 'other', 'words')
('other', 'words', 'already')
('words', 'already', 'in')
('already', 'in', 'the')
('in', 'the', 'sentence.NTK')
('the', 'sentence.NTK', 'provides')
('sentence.NTK', 'provides', 'another')
('provides', 'another', 'function')
('another', 'function', 'everygrams')
('function', 'everygrams', 'that')
('everygrams', 'that', 'converts')
('that', 'converts', 'a')
('converts', 'a', 'sentence')
('a', 'sentence', 'into')
('sentence', 'into', 'unigram,')
('into', 'unigram,', 'bigram,')
('unigram,', 'bigram,', 'trigram,')
('bigram,', 'trigram,', 'and')
('trigram,', 'and', 'so')
('and', 'so', 'on')
('so', 'on', 'till')
('on', 'till', 'the')
('till', 'the', 'ngrams,')
('the', 'ngrams,', 'where')
('ngrams,', 'where', 'n')
('where', 'n', 'is')
('n', 'is', 'the')
('is', 'the', 'length')
('the', 'length', 'of')
('length', 'of', 'the')
('of', 'the', 'sentence.')
('the', 'sentence.', 'In')
('sentence.', 'In', 'short,')
('In', 'short,', 'this')
('short,', 'this', 'function')
('this', 'function', 'generates')
('function', 'generates', 'ngrams')
('generates', 'ngrams', 'for')
('ngrams', 'for', 'all')
('for', 'all', 'possible')
('all', 'possible', 'values')
('possible', 'values', 'of')
('values', 'of', 'n.')

For sentence 1 , trigrams are: 
('While', 'unigram', 'model')
('unigram', 'model', 'sentences')
('model', 'sentences', 'will')
('sentences', 'will', 'only')
('will', 'only', 'exclude')
('only', 'exclude', 'the')
('exclude', 'the', 'UNK')
('the', 'UNK', 'token,')
('UNK', 'token,', 'models')
('token,', 'models', 'will')
('models', 'will', 'also')
('will', 'also', 'exclude')
('also', 'exclude', 'all')
('exclude', 'all', 'other')
('all', 'other', 'words')
('other', 'words', 'already')
('words', 'already', 'in')
('already', 'in', 'the')
('in', 'the', 'sentence')

For sentence 2 , trigrams are: 

('NTK', 'provides', 'another')
('provides', 'another', 'function')
('another', 'function', 'everygrams')
('function', 'everygrams', 'that')
('everygrams', 'that', 'converts')
('that', 'converts', 'a')
('converts', 'a', 'sentence')
('a', 'sentence', 'into')
('sentence', 'into', 'unigram,')
('into', 'unigram,', 'bigram,')
('unigram,', 'bigram,', 'trigram,')
('bigram,', 'trigram,', 'and')
('trigram,', 'and', 'so')
('and', 'so', 'on')
('so', 'on', 'till')
('on', 'till', 'the')
('till', 'the', 'ngrams,')
('the', 'ngrams,', 'where')
('ngrams,', 'where', 'n')
('where', 'n', 'is')
('n', 'is', 'the')
('is', 'the', 'length')
('the', 'length', 'of')
('length', 'of', 'the')
('of', 'the', 'sentence')

For sentence 3 , trigrams are: 

('', 'In', 'short,')
('In', 'short,', 'this')
('short,', 'this', 'function')
('this', 'function', 'generates')
('function', 'generates', 'ngrams')
('generates', 'ngrams', 'for')
('ngrams', 'for', 'all')
('for', 'all', 'possible')
('all', 'possible', 'values')
('possible', 'values', 'of')
('values', 'of', 'n\n')

"""