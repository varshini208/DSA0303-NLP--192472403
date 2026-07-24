import nltk
import matplotlib.pyplot as plt

text = input("Enter text: ")

words = text.split()

fd = nltk.FreqDist(words)

fd.plot()