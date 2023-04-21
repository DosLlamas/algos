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

