# arr = [1, 2, 3, 4, 5]
# for i, num in enumerate(arr):
#     num = 0
    

# print(arr)

# d = {"a": 0, "b": 1, "c": 3}
# print(d.values())


# nums = []
# for i in range(3):
#     nums.append(int(input()))

# print(nums)

# print('a'*1)

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# even_nums = [num for num in nums if num % 2 == 0] 
# print(even_nums)

# pairs = [('e', 2),('f', 9),('g',3),('h',8),('a', 4),('b', 2),('c', 6),('d', 7),('e',1),('i',0),('j', 5)]
# pairs.sort(key=lambda item: (-item[1], item[0]), reverse=True)
# print(pairs)

# people1 = {"name": "Nathan", "age": 23}
# people2 = {"name": "Nathan", "city": "Orlando"}
# merged_people = {**people1, **people2}
# print(merged_people)

# from collections import Counter

# nums = ["1", "1", "1", "3", "2", "6", "3", "9", "8", "1", "0"]
# freq = Counter(nums)
# print(freq["1"])
# print(freq.most_common(3))

# squared_nums = {str(i): i**2 for i in range(6)}
# print(squared_nums)

# tuple_comp = (i for i in range(10))
# print(tuple_comp)

# nums = {1, 2, 5, 4, 7, 3, 9, 0}
# copy_nums = nums
# copy_nums.add(6)
# print(nums)

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # def is_even(test):
# #     return test()
# # for num in nums:
# #     print(is_even(lambda: True if num % 2 == 0 else False))
# def is_even(num):
#     return True if num % 2 == 0 else False

# def sum_evens(func, is_even):
#     return 

# from typing import List
# def combine(a: List[int], b: List[int]) -> int:
#     return sum(a) + sum(b)
# print(combine([1, 2], [3, 4]))


# def reduceRecursion(arr, i, func, start):
#     if i >= len(arr):
#         return start
#     else:
#         acc = func(start, arr[i])
#         return reduceRecursion(arr, i + 1, func, acc)
    
# def reduce(arr, func, start):
#     return reduceRecursion(arr, 0, func, start)
# def reduce(arr, func, start):
#     acc = start
#     for item in arr:
#         acc = func(acc, item)
#     return acc

# nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("".join(nums))

# def add(a, b):
#     return a + b

# print(reduce(nums, lambda acc, num: acc + num, 1))

# my_dict = {"name": "Nathan"}
# print(1 if "age" in my_dict else 0)

# str1 = "Me"
# str2 = "and"
# str3 = "Ashley"
# print(f"{str1} {str2} {str3}.")

# boolean1 = True
# boolean2 = False
# print(True if boolean1 else False)
# print(True if boolean2 else False)




# nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(True if nums == nums2 else False)

# my_dict = {"name": "Nathan"}
# print(my_dict.get("city", None))
# print(True if "city" in my_dict else False)

# from collections import defaultdict
# my_dict = defaultdict(int)
# print(my_dict["age"])
# num = "1"
# num += str(my_dict["age"])
# print(num)


# my_dict2 = {"name": "Bob"}
# print(True if my_dict == my_dict2 else False)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(id(nums))
print(id(nums2))
# print(True if nums)
# nums.extend(range(1000000000000))
# print(id(nums))