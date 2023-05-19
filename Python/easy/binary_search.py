'''
Write a function that takes in a sorted array of integers as well as a target
integer. The function should use the Binary Search algorithm to determine if
the target integer is contained in the array and should return its index if it
is, otherwise return -1

Sample Input
arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]

Sample Output
3

Approach
O(log n) time
O(1) space
'''

def binarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

