"""""
Absolute Value Sort
Given an array of integers arr, write a function absSort(arr), that 
sorts the array according to the absolute values of the numbers in arr. 
If two numbers have the same absolute value, sort them according to sign, 
where the negative numbers come before the positive numbers.

Examples:

input:  arr = [2, -7, -2, -2, 0]
output: [0, -2, -2, 2, -7]
Constraints:

[time limit] 5000ms
[input] array.integer arr
0 ≤ arr.length ≤ 10
[output] array.integer


My naive approach(FAILED):
1. 
iterate arr
2.
Check if current index is greater than the next, then move current to the right
3.
Check if current is less than previous, then move current to left
4.
For both step 2 & 3, if abs value is equal, move the negative num to the left
5.
return result array

Code:
def absSort(arr):

  for i in range(len(arr)):
    if i+2 < len(arr):
      if abs(arr[i]) > abs(arr[i+1]) :
        switch = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = switch
      elif abs(arr[i]) == abs(arr[i+1]):
        if arr[i] > arr[i+1] :
          switch = arr[i+1]
          arr[i+1] = arr[i]
          arr[i] = switch
    if i - 1 >= 0 :
      if abs(arr[i] < abs(arr[i-1])) :
        switch = arr[i]
        arr[i] = arr[i-1]
        arr[i-1] = switch
      elif abs(arr[i]) == abs(arr[i-1]):
        if arr[i] < arr[i-1] :
          switch = arr[i]
          arr[i] = arr[i-1]
          arr[i-1] = switch
          
  return arr

"""""
# Correct approach
def absSort(arr):
    def compare(a, b):
        if abs(a) < abs(b): return -1
        if abs(a) > abs(b): return 1
        if a < b: return -1
        if a > b: return 1
        return 0

    arr.sort(cmp = compare)
    return arr

test_arr = [2, -7, -2, -2, 0]
print(absSort(test_arr))

# Leverage the sort function of your languages library. 
# Usually, it will have support for either a custom comparison function.

# For a custom comparison function compare(a, b), 
# typically we want to return -1 if a < b, 1 if a > b, and 0 if a == b.

# Time Complexity: O(N log N), the complexity of sorting.

# Space Complexity: O(N), the space typically used by compilers
# in their implementation of sorting operations.


# Approach 2
# Write a custom comparison function, such as smaller(a, b)
# which is true if and only if a is supposed to come before
# b (and a != b). From here, we can repeatedly find the
# ‘smallest’ number in A[i], A[i+1], ..., A[A.length - 1]
# and swapping it with A[i].

# def absSort2(arr):
#     def smaller(a, b):
#         if abs(a) < abs(b): return true
#         if abs(a) > abs(b): return false
#         return a < b

#     for i from 0 to arr.length - 2:
#         best = i
#         for j from i to arr.length - 1:
#             if smaller(arr[j], arr[best]):
#                 best = j
#         arr[best], arr[i] = arr[i], arr[best]

#     return arr
# Time Complexity: O(N^2) from our two for loops.

# Space Complexity: O(1), the additional space used by best.

