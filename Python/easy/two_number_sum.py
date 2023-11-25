# Write a function that takes in a non-empty array of distinct integers and an
# integer representing a target sum. If any two numbers in the input array sum
# up to the target sum, the function should return them in an array, in any
# order. If no two numbers sum up to the target sum, the function should return
# an empty array.
# Note that the target sum has to be obtained by summing two different integers
# in the array; you can't add a single integer to itself in order to obtain the
# target sum.
# You can assume that there will be at most one pair of numbers summing up to
# the target sum.

def twoNumberSum(array, targetSum):
    for num1 in array:
        for num2 in array:
            if num1 != num2 :
                if num1 + num2 == targetSum :
                    return [num1, num2]
    return []



# Test case  
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# target = 10

"""
1.
This approach takes O(n**2) time because of the nested for loop
2.
Not sure of a more optimal answer yet

Appraoch 2:

Steps:
1.
copy list to a set
2.
iterate through list
3.
check if current num - targetSum equals anything in the set
4.
if yes, return those, if no return emptpy list

O(n) time | O(n) space
"""

def twoNumberSum2(array, targetSum):
    storage = set()
    for first_num in array:
        storage.update({first_num})
        second_num = targetSum - first_num
        if second_num in storage and not second_num is first_num:
            return [first_num, second_num]
    return []

arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
target2 = 12


print(twoNumberSum2(arr, target2))
