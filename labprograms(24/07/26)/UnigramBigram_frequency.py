from collections import Counter
text = input("Enter text: ")
words = text.split()
unigram = Counter(words)
bigram = []

for i in range(len(words)-1):
    bigram.append((words[i], words[i+1]))
bigram_count = Counter(bigram)
print("Unigram:", unigram)
print("Bigram:", bigram_count)