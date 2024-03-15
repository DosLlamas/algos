'''
Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent
in the array but that are in the same order as they appear in the array. For
instance, the numbers

Sample Input
  array = [5,1,22,25,6,-1,8,10]
  sequence = [1,6,-1,10]

Sample Output
  true


Approach O(n) time O(1) space
'''

def isValidSubsequence(array, sequence):
    sequence_pointer = 0
    for num in array:
        if sequence_pointer == len(sequence):
            return True
        if sequence[sequence_pointer] == num:
            sequence_pointer += 1
    return sequence_pointer == len(sequence)
            
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],  [1, 6, -1, 10]))
