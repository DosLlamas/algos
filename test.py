import sys

# Example variables
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_dict = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}

# Get the size of each variable
print("Size of my_list:", sys.getsizeof(my_list), "bytes")
print("Size of my_dict:", sys.getsizeof(my_dict), "bytes")