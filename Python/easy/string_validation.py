""""
These are the coding questions I was asked in
a Data Analyst interview.

1.
Given string = "AalksndfoiAIASpfihasdlfoAWLOIRHEsdfd",
count how many vowels appear, upper and lowercase

2.
Write a function that validates an email, return true
if valid, false if not valid
"""

def count_vowels(str):
    count = 0
    for char in str :
        if char.lower() in ['a', 'e', 'i', 'o', 'u'] :
            count += 1
    return count

print(count_vowels("AalksndfoiAIASpfihasdlfoAWLOIRHEsdfd"))

def is_valid_email(user_email):
    if not user_email :
        return False
    username, domain_name = user_email.split("@")
    if username.endswith(".") or username.startswith(".") :
        return False
    if domain_name.endswith(".") or domain_name.startswith(".") :
        return False
    

print(is_valid_email("tt@gmail.com"))
    





