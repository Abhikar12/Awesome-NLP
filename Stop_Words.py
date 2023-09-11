"""
Assignment No 1 
Name - Abhishek Kusalkar
Batch - B2
Roll No - 35
Assignment Title : Text pre-processing using NLP operation : perform Tokenization Stop word removal, Punctuation removal,using Spacy or NLTK Library 

"""

# Import the necessary libraries
import spacy

# Load the English language model for spaCy
nlp=spacy.load("en_core_web_sm")
from collections import Counter

# Define the custom text you want to process
custom_about_text = (
    
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

# Load the English language model for spaCy again (This line is redundant, you can remove it)
nlp = spacy.load("en_core_web_sm")

# Process the custom text using spaCy
about_doc = nlp(custom_about_text)

# Print the tokens in the document that are not stop words
print([token for token in about_doc if not token.is_stop])

    
# OUTPUT -

"""

[smile, makes, smile, ,, laugh, makes, laugh, ,, eyes, enchanting, ,, thoughts, daft, ., day, laid, eyes, ,, feelings, grew, grew, ., conversation, knees, clicked, clacked, ,, butterflies, flipped, flapped, ., spill, simple, rhymes, ,, mind, goes, time, time, ,, crush, ,, little, teenage, crushI, know, ,, lovely, little, crush]

"""