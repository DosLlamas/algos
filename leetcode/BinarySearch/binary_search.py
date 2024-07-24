'''
Write a function that takes in a sorted array of integers as well as a target
integer. The function should use the Binary Search algorithm to determine if
the target integer is contained in the array and should return its index if it
is, otherwise return -1

Sample Input
arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
num = 33
Sample Output
3

Approach
O(log n) time
O(1) space

Steps:
1.
left and right pointer
2.
while the left is less than right,
3.
is mid point is the target, greater or less?
4.
move the appropriate pointer to mid and repeat 2
'''

def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if array[mid] == target:
        return mid
    return -1

arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target_num = int(input("Enter a number: "))
ans = binarySearch(arr, target_num)
if ans == -1:
    print("num not in the list")
else:
    print(f"num in list at index: {ans}")
    


