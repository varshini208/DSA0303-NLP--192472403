from collections import defaultdict

text = input("Enter sentence: ")

words = text.split()
bigrams = defaultdict(list)

for i in range(len(words) - 1):
    bigrams[words[i]].append(words[i + 1])

print("Bigram Model:")
for word, next_words in bigrams.items():
    print(word, "->", next_words)