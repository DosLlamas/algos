# Check if a string is a palindrome, return "YES" or "NO"
def isPalindrome(string):
    start = 0
    end = len(string) - 1
    while start < end :
        if string[start] != string[end] :
            return "NO"
        start += 1
        end -= 1

    return "YES"


# test1 = "tacocat"
# test2 = "level"
# test3 = "not"

inp = input("Enter a word or palindrome: ")

print(isPalindrome(inp))
# print(isPalindrome(test2))
# print(isPalindrome(test3))
