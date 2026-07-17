import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()
word = input("Enter a word: ")
print("Stem word:", ps.stem(word))