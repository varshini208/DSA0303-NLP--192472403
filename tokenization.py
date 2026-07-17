import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize

text = input("Enter the paragraph: ")

sentences = sent_tokenize(text)

print(sentences)