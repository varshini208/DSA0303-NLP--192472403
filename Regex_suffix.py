import re
word = input("Enter a word: ")
suffix = re.findall(r'(ing|ed|ly|s)$', word)
print("Suffix:", suffix)