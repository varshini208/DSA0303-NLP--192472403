from collections import Counter
text = input("Enter text: ")
words = text.split()
frequency = Counter(words)
print(frequency)