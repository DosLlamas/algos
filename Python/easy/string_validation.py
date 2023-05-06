""""
These are the coding questions I was asked in
a Data Analyst interview.

Question 1.
Given string = "AalksndfoiAIASpfihasdlfoAWLOIRHEsdfd",
count how many vowels appear, upper and lowercase

Approach:
-O(n) time
-O(n) space at worst
Steps:
1.
set count = 0
2.
increase count per vowel
3.
return count

Tradeoffs:
Is there a way to check for vowels without 
passing through the entire string? A binary search 
instead of simple search? 

Question 2.
Using regex, write a function that validates an email, return true
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
    





