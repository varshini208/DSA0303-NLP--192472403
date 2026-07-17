import re
word = input("Enter a word: ")
match = re.search(r'(ing|ed|ly|es|s)$', word)
if match:
    suffix = match.group()
    root = word[:-len(suffix)]
    print("Root word:", root)
    print("Suffix:", suffix)
else:
    print("Root word:", word)
    print("No suffix found")