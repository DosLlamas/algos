# Check if a string is a palindrome, return True or False
def isPalindrome(string):
    start = 0
    end = len(string) - 1
    while start < end :
        if string[start] != string[end] :
            return False
        start += 1
        end -= 1

    return True

# test1 = "tacocat"
# test2 = "level"
# test3 = "not"

inp = input("Enter a word or palindrome: ")

# print(isPalindrome(inp))
# print(isPalindrome(test2))
# print(isPalindrome(test3))

# Solution 2:
"""
Solution 2 uses the built in method within Python, slice()
Steps:
1.
Reverse the string's order
2.
Check if equal to original input
3.
Return "YES" or "NO"

Edge cases:
1. 
This solution falters if we also need to return the index
of the character that was different, so solution 1 wins in that
way
2.
This solution still takes O(n) time becuase the slice
method will iterate through the whole input once
3. 
This solution takes less space because there's no need to declare 
any more variables
"""

def isPalindrome2(str):
    return str == str[::-1] 
    # reverse = str.reverse()
    # if str == reverse:
    #     return "YES"
    # else:
    #     return "NO"
    
print(isPalindrome2(inp))

