from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = input("Enter words: ").split()

for word in words:
    print(word, "->", stemmer.stem(word))