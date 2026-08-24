import nltk
import spacy
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
from nltk import word_tokenize, pos_tag
# Load spaCy model
nlp = spacy.load("en_core_web_sm")
# User input
text = input("Enter a sentence: ")
# NLTK POS Tagging
tokens = word_tokenize(text)
nltk_tags = pos_tag(tokens)
# spaCy POS Tagging
doc = nlp(text)

print("\nNLTK POS Tags")
for word, tag in nltk_tags:
    print(word, ":", tag)

print("\nspaCy POS Tags")
for token in doc:
    print(token.text, ":", token.pos_)