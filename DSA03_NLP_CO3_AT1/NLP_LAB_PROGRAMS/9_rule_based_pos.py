import re

def tag_word(word):
    if re.match(r'.*ing$', word):
        return "VBG"
    elif re.match(r'.*ed$', word):
        return "VBD"
    elif re.match(r'.*ly$', word):
        return "RB"
    else:
        return "NN"

words = input("Enter words: ").split()

for word in words:
    print(word, "->", tag_word(word))