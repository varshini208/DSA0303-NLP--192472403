import nltk
from nltk import word_tokenize, pos_tag

text = input("Enter sentence: ")

tokens = word_tokenize(text)
tags = pos_tag(tokens)

print("POS Tags:")
for word, tag in tags:
    print(word, "->", tag)