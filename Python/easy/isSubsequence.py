"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new 
string that is formed from the original string 
by deleting some (can be none) of the characters
 without disturbing the relative positions of the 
 remaining characters. (i.e., "ace" is a subsequence 
 of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true


Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.
"""
def isSubsequence(s, t):
    """
    rules:
    -return true or false
    -return true is s is empty
    -return true if s is in t, but in the same order

    steps:
    1.
    if s is empty, return true
    2.
    declare pointer for s
    3.
    iterate t.
    on each iteration we check if the letter is same.
    if yes, move to next letter in s
    if we point at last letter of s,
    return true

    4.
    return false if we iterate through all of t

    complexity:
    O(n) time | O(1) space
    """
    if len(s) == 0: return True
    s_pointer = 0
    for char in t:
        if char == s[s_pointer]:
            s_pointer += 1
        if s_pointer == len(s):
            return True
    return False

print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("", "ahbgdc"))