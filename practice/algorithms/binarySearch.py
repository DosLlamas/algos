arr = [1, 2, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def binarySearch(arr, target, l, r):
    if l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target: return mid ## base case
        elif arr[mid] > target:
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        return binarySearch(arr, target, l, r) ## recursive case
    return -1

print("Index of target: ", binarySearch(arr, 7, 0, len(arr) - 1))