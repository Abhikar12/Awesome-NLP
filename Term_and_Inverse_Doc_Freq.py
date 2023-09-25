"""
Assignment No 
Name - Abhishek Kusalkar
Batch - B2
Roll No - 35
Assignment Title : Natural Language Processing (NLP) using Gensim

"""

import numpy as np
from gensim.utils import simple_preprocess
from gensim import corpora
from gensim import models

text = ["Your smile makes me smile,"
    "Your laugh makes me laugh,"
    "Your eyes are enchanting,"
    "You make my thoughts seem daft."
    "Since the day I first laid eyes on you,"
    "My feelings grew and grew."
    "In that first conversation my knees clicked and clacked,"
    "And those butterflies flipped and flapped."
    "And as I spill these simple rhymes,"
    "My mind goes over time and time,"
    "I have a crush, a little teenage crush"
    "I don't know what to do, about this lovely little crush"]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])

# OUTPUT -
"""

Dictionary :

[['about', 1], ['and', 6], ['are', 1], ['as', 1], ['butterflies', 1], ['clacked', 1], ['clicked', 1], ['conversation', 1], ['crush', 2], ['crushi', 1], ['daft', 1], ['day', 1], ['do', 1], ['don', 1], ['enchanting', 1], ['eyes', 2], ['feelings', 1], ['first', 2], ['flapped', 1], ['flipped', 1], ['goes', 1], ['grew', 2], ['have', 1], ['in', 1], ['knees', 1], ['know', 1], ['laid', 1], ['laugh', 2], ['little', 2], ['lovely', 1], ['make', 1], ['makes', 2], ['me', 2], ['mind', 1], ['my', 4], ['on', 1], ['over', 1], ['rhymes', 1], ['seem', 1], ['simple', 1], ['since', 1], ['smile', 2], ['spill', 1], ['teenage', 1], ['that', 1], ['the', 1], ['these', 1], ['this', 1], ['those', 1], ['thoughts', 1], ['time', 2], ['to', 1], ['what', 1], ['you', 2], ['your', 3]]

TF-IDF Vector:

[['about', 0.08], ['and', 0.5], ['are', 0.08], ['as', 0.08], ['butterflies', 0.08], ['clacked', 0.08], ['clicked', 0.08], ['conversation', 0.08], ['crush', 0.17], ['crushi', 0.08], ['daft', 0.08], ['day', 0.08], ['do', 0.08], ['don', 0.08], ['enchanting', 0.08], ['eyes', 0.17], ['feelings', 0.08], ['first', 0.17], ['flapped', 0.08], ['flipped', 0.08], ['goes', 0.08], ['grew', 0.17], ['have', 0.08], ['in', 0.08], ['knees', 0.08], ['know', 0.08], ['laid', 0.08], ['laugh', 0.17], ['little', 0.17], ['lovely', 0.08], ['make', 0.08], ['makes', 0.17], ['me', 0.17], ['mind', 0.08], ['my', 0.33], ['on', 0.08], ['over', 0.08], ['rhymes', 0.08], ['seem', 0.08], ['simple', 0.08], ['since', 0.08], ['smile', 0.17], ['spill', 0.08], ['teenage', 0.08], ['that', 0.08], ['the', 0.08], ['these', 0.08], ['this', 0.08], ['those', 0.08], ['thoughts', 0.08], ['time', 0.17], ['to', 0.08], ['what', 0.08], ['you', 0.17], ['your', 0.25]]

"""