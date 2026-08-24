from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

word = input("Enter word: ")

print("Word:", word)
print("Root/Stem:", stemmer.stem(word))