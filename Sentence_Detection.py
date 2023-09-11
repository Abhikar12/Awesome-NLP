"""

Assignment No 1 
Name - Abhishek Kusalkar
Batch - B2
Roll No - 35
Assignment Title : Text pre-processing using NLP operation : perform Tokenization Stop word removal, Punctuation removal,using Spacy or NLTK Library 

"""

# Import the necessary libraries
import spacy

# Import the necessary libraries
nlp=spacy.load("en_core_web_sm")
from collections import Counter

# Define a text containing a poem or a set of sentences
about_text = (
    "Your smile makes me smile,"
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
    "I don't know what to do, about this lovely little crush"
)

# Process the text using the spaCy model
about_doc = nlp(about_text)

# Split the text into individual sentences
sentences = list(about_doc.sents)

# Print the number of sentences in the text
len(sentences)

# Iterate through each sentence and print the first 5 characters of each sentence

for sentence in sentences:
    print(f"{sentence[:5]}...")
    
    
# OUTPUT -

"""
    Your smile makes me smile...
    Since the day I first...
    In that first conversation my...
    And as I spill these...
    
"""

 
 
 
 
 
