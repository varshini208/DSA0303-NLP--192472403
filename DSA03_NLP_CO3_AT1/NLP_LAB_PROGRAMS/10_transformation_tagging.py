words = input("Enter words: ").split()

tags = []

for word in words:
    if word.endswith("ing"):
        tags.append("VBG")
    else:
        tags.append("NN")

print("Initial Tags:")
for word, tag in zip(words, tags):
    print(word, "->", tag)

# Transformation rule
for i in range(len(words)):
    if words[i] == "running":
        tags[i] = "VBG"

print("\nFinal Tags:")
for word, tag in zip(words, tags):
    print(word, "->", tag)