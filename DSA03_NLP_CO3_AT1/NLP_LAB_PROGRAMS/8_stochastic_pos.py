probability = {
    "book": {"NN": 0.4, "VB": 0.6},
    "run": {"NN": 0.3, "VB": 0.7},
    "student": {"NN": 0.9}
}

word = input("Enter word: ").lower()

if word in probability:
    tag = max(probability[word], key=probability[word].get)
    print("POS Tag:", tag)
    print("Probability:", probability[word][tag])
else:
    print("Word not found")