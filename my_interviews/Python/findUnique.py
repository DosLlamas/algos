test1 = [5, 65, 4, 8, 13, 27]

test2 = [5, 65, 4, 8, 13, 27,12,]


def findUnique(arr1, arr2):
  for i in range(len(arr1)):
    if arr1[i] != arr2[i]:
      return arr2[i]
  return arr2[-1]

print(findUnique(test1, test2))

def find_unique_number(list1, list2):
    result = 0

    # XOR all numbers in the first list
    for num in list1:
        result ^= num

    # XOR all numbers in the second list
    for num in list2:
        result ^= num

    return result

print(find_unique_number(test1, test2))


def find_unique2(test1, test2):
    return sum(test2) - sum(test1)

print(find_unique2(test1, test2))