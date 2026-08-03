from collections import defaultdict
# Corpus
corpus = [
    "Students learn NLP",
    "Students learn Python",
    "Students write Code",
    "Teachers teach NLP",
    "Teachers teach Python"
]
# Build vocabulary
words = []
for sentence in corpus:
    words.extend(sentence.split())

vocab = set(words)
V = len(vocab)
# Count unigrams
unigram = defaultdict(int)
for word in words:
    unigram[word] += 1
# Count bigrams
bigram = defaultdict(int)
for sentence in corpus:
    tokens = sentence.split()
    for i in range(len(tokens) - 1):
        bigram[(tokens[i], tokens[i + 1])] += 1
# Function to calculate Laplace Probability
def laplace(previous_word, next_word):
    count_bigram = bigram[(previous_word, next_word)]
    count_previous = unigram[previous_word]
    probability = (count_bigram + 1) / (count_previous + V)
    return probability
# Display counts
print("Vocabulary Size =", V)
print()

print("Unigram Counts")
for word, count in unigram.items():
    print(word, ":", count)

print("\nBigram Counts")
for pair, count in bigram.items():
    print(pair, ":", count)

# Calculate probabilities
print("\nLaplace Probabilities")
print("P(learn | Students) =", laplace("Students", "learn"))
print("P(write | Students) =", laplace("Students", "write"))
print("P(Code | learn) =", laplace("learn", "Code"))