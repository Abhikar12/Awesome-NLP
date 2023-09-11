"""
Assignment No 1 
Name - Abhishek Kusalkar
Batch - B2
Roll No - 35
Assignment Title : Text pre-processing using NLP operation : perform Tokenization Stop word removal, Punctuation removal,using Spacy or NLTK Library 

"""

# Import the Spacy library
import spacy

# Load the English language model "en_core_web_sm"
nlp = spacy.load("en_core_web_sm")

# Define the text you want to analyze
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

# Process the text using Spacy to create a Doc object
about_doc = nlp(about_text)

# Iterate through each token in the processed document
for token in about_doc:

    # Print information about each token, including its text, part-of-speech tag, and an explanation of the tag
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )

    
# OUTPUT -

"""

TOKEN: Your
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: smile
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: makes
=====
TAG: VBZ        POS: VERB
EXPLANATION: verb, 3rd person singular present

TOKEN: me
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: smile
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: Your
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: laugh
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: makes
=====
TAG: VBZ        POS: VERB
EXPLANATION: verb, 3rd person singular present

TOKEN: me
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: laugh
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: Your
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: eyes
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: are
=====
TAG: VBP        POS: AUX
EXPLANATION: verb, non-3rd person singular present

TOKEN: enchanting
=====
TAG: VBG        POS: VERB
EXPLANATION: verb, gerund or present participle

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: You
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: make
=====
TAG: VBP        POS: VERB
EXPLANATION: verb, non-3rd person singular present

TOKEN: my
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: thoughts
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: seem
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: daft
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: Since
=====
TAG: IN         POS: SCONJ
EXPLANATION: conjunction, subordinating or preposition

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: day
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: I
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: first
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: laid
=====
TAG: VBD        POS: VERB
EXPLANATION: verb, past tense

TOKEN: eyes
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: on
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: you
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: My
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: feelings
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: grew
=====
TAG: VBD        POS: VERB
EXPLANATION: verb, past tense

TOKEN: and
=====
TAG: CC         POS: CCONJ
EXPLANATION: conjunction, coordinating

TOKEN: grew
=====
TAG: VBD        POS: VERB
EXPLANATION: verb, past tense

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: In
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: that
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: first
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: conversation
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: my
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: knees
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: clicked
=====
TAG: VBD        POS: VERB
EXPLANATION: verb, past tense

TOKEN: and
=====
TAG: CC         POS: CCONJ
EXPLANATION: conjunction, coordinating

TOKEN: clacked
=====
TAG: VBN        POS: VERB
EXPLANATION: verb, past participle

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: And
=====
TAG: CC         POS: CCONJ
EXPLANATION: conjunction, coordinating

TOKEN: those
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: butterflies
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: flipped
=====
TAG: VBD        POS: VERB
EXPLANATION: verb, past tense

TOKEN: and
=====
TAG: CC         POS: CCONJ
EXPLANATION: conjunction, coordinating

TOKEN: flapped
=====
TAG: VBD        POS: VERB
EXPLANATION: verb, past tense

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: And
=====
TAG: CC         POS: CCONJ
EXPLANATION: conjunction, coordinating

TOKEN: as
=====
TAG: IN         POS: SCONJ
EXPLANATION: conjunction, subordinating or preposition

TOKEN: I
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: spill
=====
TAG: VBP        POS: VERB
EXPLANATION: verb, non-3rd person singular present

TOKEN: these
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: simple
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: rhymes
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: My
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: mind
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: goes
=====
TAG: VBZ        POS: VERB
EXPLANATION: verb, 3rd person singular present

TOKEN: over
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: time
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: and
=====
TAG: CC         POS: CCONJ
EXPLANATION: conjunction, coordinating

TOKEN: time
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: I
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: have
=====
TAG: VBP        POS: VERB
EXPLANATION: verb, non-3rd person singular present

TOKEN: a
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: crush
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: a
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: little
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: teenage
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: crushI
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: do
=====
TAG: VBP        POS: AUX
EXPLANATION: verb, non-3rd person singular present

TOKEN: n't
=====
TAG: RB         POS: PART
EXPLANATION: adverb

TOKEN: know
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: what
=====
TAG: WP         POS: PRON
EXPLANATION: wh-pronoun, personal

TOKEN: to
=====
TAG: TO         POS: PART
EXPLANATION: infinitival "to"

TOKEN: do
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: about
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: this
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: lovely
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: little
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: crush
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

"""

