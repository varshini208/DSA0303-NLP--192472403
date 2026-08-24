def check_string(s):
    if s.endswith("ab"):
        return "Accepted"
    return "Rejected"

s = input("Enter string: ")
print("Result:", check_string(s))