corpus = []
n = int(input("Enter number of sentences: "))
for i in range(n):
    sentence = input("Enter sentence: ")
    corpus.append(sentence)
print("Corpus:")
for s in corpus:
    print(s)