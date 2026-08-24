import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
from nltk import word_tokenize, pos_tag
sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)

print("\nPOS Tags:")
for word, tag in tags:
    print(word, ":", tag)