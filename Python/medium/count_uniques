# Count Numbers with Unique Digits
# Medium
# Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

# Example 1:

# Input: n = 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
# Example 2:

# Input: n = 0
# Output: 1
 

# Constraints:

# 0 <= n <= 8
# def countNumbersWithUniqueDigits(n):
#   """
#   :type n: int
#   :rtype: int

#   time complexity: O(10^n)
#   space: O(10^n)
#   Trade off, really bad answer. This is 
#   some algebra. To find count
#   without iterating over the range, you would need 
#   a formula to dynamically find the count every time. 
#   What's the formula? I would need to consult 
#   outside resources for this one. 
#   """
#   if n == 0:
#     return 1
#   count = 0
#   for i in range(0, (10**n)):
#     if n % 11 != 0 or n == 0:
#         count += 1
#   return count
    
# test = 2
# print(countNumbersWithUniqueDigits(test))