text = input("Enter text: ")
words = text.split()
first = input("Enter first word: ")
second = input("Enter second word: ")
first_count = words.count(first)
bigram_count = 0

for i in range(len(words)-1):
    if words[i] == first and words[i+1] == second:
        bigram_count += 1

if first_count > 0:
    probability = bigram_count / first_count
    print("Probability =", probability)
else:
    print("Word not found")