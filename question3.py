import re
text = input("Enter the paragraph: ")

dates = re.findall(r'\d{2}/\d{2}/\d{4}', text)
phones = re.findall(r'[6-9]\d{9}', text)
hashtags = re.findall(r'#\w+', text)
mentions = re.findall(r'@\w+', text)

print("Dates:", dates)
print("Phone Numbers:", phones)
print("Hashtags:", hashtags)
print("Mentions:", mentions)
