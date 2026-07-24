import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
text = input("Enter a sentence: ")
tokens = word_tokenize(text)
print("Tokens:", tokens)