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

text2 = open('Bag.txt', encoding ='utf-8')
 
tokens2 =[]
for line in text2.read().split('.'):
  tokens2.append(simple_preprocess(line, deacc = True))

g_dict2 = corpora.Dictionary(tokens2)

print("The dictionary has: " +str(len(g_dict2)) + " tokens\n")
print(g_dict2.token2id)

#Using Bag-of-Words(BOW)
g_bow =[g_dict2.doc2bow(token, allow_update = True) for token in tokens2]      
print("Bag of Words : ", g_bow)

# OUTPUT -
"""
The dictionary has: 54 tokens

{'are': 0, 'daft': 1, 'enchanting': 2, 'eyes': 3, 'laugh': 4, 'make': 5, 'makes': 6, 'me': 7, 'my': 8, 'seem': 9, 'smile': 10, 'thoughts': 11, 'you': 12, 'your': 13, 'and': 14, 'day': 15, 'feelings': 16, 'first': 17, 'grew': 18, 'laid': 19, 'on': 20, 'since': 21, 'the': 22, 'butterflies': 23, 'clacked': 24, 'clicked': 25, 'conversation': 26, 'flapped': 27, 'flipped': 28, 'in': 29, 'knees': 30, 'that': 31, 'those': 32, 'about': 33, 'as': 34, 'crush': 35, 'do': 36, 'don': 37, 'goes': 38, 'have': 39, 'know': 40, 'little': 41, 'lovely': 42, 'mind': 43, 'over': 44, 'rhymes': 45, 'simple': 46, 'spill': 47, 'teenage': 48, 'these': 49, 'this': 50, 'time': 51, 'to': 52, 'what': 53}
Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 2), (5, 1), (6, 2), (7, 2), (8, 1), (9, 1), (10, 2), (11, 1), (12, 1), (13, 3)], [(3, 1), (8, 1), (12, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 2), (19, 1), (20, 1), (21, 1), (22, 1)], [(8, 1), (14, 3), (17, 1), (23, 1), (24, 1), (25, 1), (26, 1), (27, 1), (28, 1), (29, 1), (30, 1), (31, 1), (32, 1)], [(8, 1), (14, 2), (33, 1), (34, 1), (35, 3), (36, 1), (37, 1), (38, 1), (39, 1), (40, 1), (41, 2), (42, 1), (43, 1), (44, 1), (45, 1), (46, 1), (47, 1), (48, 1), (49, 1), (50, 1), (51, 2), (52, 1), (53, 1)]]

"""
