"""
Assignment No 1 
Name - Abhishek Kusalkar
Batch - B2
Roll No - 35
Assignment Title : Text pre-processing using NLP operation : perform Tokenization Stop word removal, Punctuation removal,using Spacy or NLTK Library 

"""

# Import the spaCy library
import spacy

# Import Counter class from the collections module
from collections import Counter

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")

# Define the complete text you want to analyze
complete_text = (
    
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

# Process the complete text using spaCy's language model
complete_doc = nlp(complete_text)

# Create a list of words from the processed document, excluding stop words and punctuation

words = [
    token.text
    for token in complete_doc
    if not token.is_stop and not token.is_punct
]

# Print the most common 5 words and their frequencies
print(Counter(words).most_common(5))
    
# OUTPUT -

"""
    [('smile', 2), ('makes', 2), ('laugh', 2), ('eyes', 2), ('grew', 2)]
    
"""
 
 
 
 
 
