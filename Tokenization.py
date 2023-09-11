"""
Assignment No 1 
Name - Abhishek Kusalkar
Batch - B2
Roll No - 35
Assignment Title : Text pre-processing using NLP operation : perform Tokenization Stop word removal, Punctuation removal,using Spacy or NLTK Library 

"""

# Import the spaCy library
import spacy

# Load the English language model "en_core_web_sm" provided by spaCy
nlp = spacy.load("en_core_web_sm")

# Define the text you want to analyze
about_text = (
    
    "Your smile makes me smile"
    "Your laugh makes me laugh"
    "Your eyes are enchanting"
    "You make my thoughts seem daft."
    "Since the day I first laid eyes on you,"
    "My feelings grew and grew."
    "In that first conversation my knees clicked and clacked,"
    "And those butterflies flipped and flapped."
    "And as I spill these simple rhymes"
    "My mind goes over time and time,"
    "I have a crush, a little teenage crush"
    "I don't know what to do, about this lovely little crush"
    
)

# Process the text using the spaCy pipeline
about_doc = nlp(about_text)

# Iterate through each token in the processed document and print the token and its index

for token in about_doc:
    print (token, token.idx)
    
    
# OUTPUT -
    
"""
    
Your 0
smile 5
makes 11
me 17
smileYour 20
laugh 30
makes 36
me 42
laughYour 45
eyes 55
are 60
enchantingYou 64
make 78
my 83
thoughts 86
seem 95
daft 100
. 104
Since 105
the 111
day 115
I 119
first 121
laid 127
eyes 132
on 137
you 140
, 143
My 144
feelings 147
grew 156
and 161
grew 165
. 169
In 170
that 173
first 178
conversation 184
my 197
knees 200
clicked 206
and 214
clacked 218
, 225
And 226
those 230
butterflies 236
flipped 248
and 256
flapped 260
. 267
And 268
as 272
I 275
spill 277
these 283
simple 289
rhymesMy 296
mind 305
goes 310
over 315
time 320
and 325
time 329
, 333
I 334
have 336
a 341
crush 343
, 348
a 350
little 352
teenage 359
crushI 367
do 374
n't 376
know 380
what 385
to 390
do 393
, 395
about 397
this 403
lovely 408
little 415
crush 422
    
"""