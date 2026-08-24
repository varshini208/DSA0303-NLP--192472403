import re

text = input("Enter text: ")

numbers = re.findall(r'\d+', text)
emails = re.findall(r'\w+@\w+\.\w+', text)

print("Numbers:", numbers)
print("Emails:", emails)