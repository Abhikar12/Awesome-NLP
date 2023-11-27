"""
Assignment No 
Name - Abhishek Kusalkar
Batch - B2
Roll No - 35
Assignment Title : Implement and visualize Dependency Parsing of Textual Input using Standford CoreNLP and Spacy library

"""

import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

multiline_text = """
Your smile makes me smile,
Your laugh makes me laugh,
Your eyes are enchanting,
You make my thoughts seem daft.
"""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")

# OUTPUT -

"""
TOKEN: 

=====
token.tag_ = '_SP'
token.head.text = 'Your'
token.dep_ = 'dep'

TOKEN: Your
=====
token.tag_ = 'PRP$'
token.head.text = 'smile'
token.dep_ = 'poss'

TOKEN: smile
=====
token.tag_ = 'NN'
token.head.text = 'makes'
token.dep_ = 'nsubj'

TOKEN: makes
=====
token.tag_ = 'VBZ'
token.head.text = 'makes'
token.dep_ = 'ccomp'

TOKEN: me
=====
token.tag_ = 'PRP'
token.head.text = 'smile'
token.dep_ = 'nsubj'

TOKEN: smile
=====
token.tag_ = 'VB'
token.head.text = 'makes'
token.dep_ = 'ccomp'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'makes'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = ','
token.dep_ = 'dep'

TOKEN: Your
=====
token.tag_ = 'PRP$'
token.head.text = 'laugh'
token.dep_ = 'poss'

TOKEN: laugh
=====
token.tag_ = 'NN'
token.head.text = 'makes'
token.dep_ = 'nsubj'

TOKEN: makes
=====
token.tag_ = 'VBZ'
token.head.text = 'make'
token.dep_ = 'ccomp'

TOKEN: me
=====
token.tag_ = 'PRP'
token.head.text = 'laugh'
token.dep_ = 'nsubj'

TOKEN: laugh
=====
token.tag_ = 'VB'
token.head.text = 'makes'
token.dep_ = 'ccomp'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'enchanting'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = ','
token.dep_ = 'dep'

TOKEN: Your
=====
token.tag_ = 'PRP$'
token.head.text = 'eyes'
token.dep_ = 'poss'

TOKEN: eyes
=====
token.tag_ = 'NNS'
token.head.text = 'are'
token.dep_ = 'nsubj'

TOKEN: are
=====
token.tag_ = 'VBP'
token.head.text = 'enchanting'
token.dep_ = 'aux'

TOKEN: enchanting
=====
token.tag_ = 'VBG'
token.head.text = 'makes'
token.dep_ = 'ccomp'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'make'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = ','
token.dep_ = 'dep'

TOKEN: You
=====
token.tag_ = 'PRP'
token.head.text = 'make'
token.dep_ = 'nsubj'

TOKEN: make
=====
token.tag_ = 'VBP'
token.head.text = 'make'
token.dep_ = 'ROOT'

TOKEN: my
=====
token.tag_ = 'PRP$'
token.head.text = 'thoughts'
token.dep_ = 'poss'

TOKEN: thoughts
=====
token.tag_ = 'NNS'
token.head.text = 'seem'
token.dep_ = 'nsubj'

TOKEN: seem
=====
token.tag_ = 'VB'
token.head.text = 'make'
token.dep_ = 'ccomp'

TOKEN: daft
=====
token.tag_ = 'NN'
token.head.text = 'seem'
token.dep_ = 'oprd'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'make'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'

Using the 'dep' visualizer
Serving on http://0.0.0.0:5000 ...

127.0.0.1 - - [27/Nov/2023 16:47:30] "GET / HTTP/1.1" 200 20932
127.0.0.1 - - [27/Nov/2023 16:47:30] "GET /favicon.ico HTTP/1.1" 200 20932

"""