"""
Assignment No 1 
Name - Abhishek Kusalkar
Batch - B2
Roll No - 35
Assignment Title : Text pre-processing using NLP operation : perform Tokenization Stop word removal, Punctuation removal,using Spacy or NLTK Library 

"""

# Import the spaCy library
import spacy

# Load the English language model for spaCy
nlp = spacy.load("en_core_web_sm")

# Define a text containing a poem about having a crush
conference_help_text = (
    
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

# Process the text using spaCy
conference_help_doc = nlp(conference_help_text)

# Iterate through each token in the processed document
for token in conference_help_doc:
    if str(token) != str(token.lemma_):

        # Print the token's original text and its lemma
        print(f"{str(token):>20} : {str(token.lemma_)}")

    
# OUTPUT -
"""
  Your : your
               makes : make
                  me : I
                Your : your
               makes : make
                  me : I
                Your : your
                eyes : eye
                 are : be
          enchanting : enchant
                 You : you
            thoughts : thought
               Since : since
                laid : lay
                eyes : eye
                  My : my
            feelings : feeling
                grew : grow
                grew : grow
                  In : in
               knees : knee
             clicked : click
             clacked : clack
                 And : and
         butterflies : butterfly
             flipped : flip
             flapped : flap
                 And : and
              rhymes : rhyme
                  My : my
                goes : go
              crushI : crushi
                 n't : not

"""
