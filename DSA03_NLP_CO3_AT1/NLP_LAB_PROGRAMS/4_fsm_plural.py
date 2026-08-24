def plural(word):
    if word.endswith(("s", "x", "ch", "sh")):
        return word + "es"
    else:
        return word + "s"

word = input("Enter noun: ")

print("Plural:", plural(word))