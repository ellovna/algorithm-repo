
# Given a list of random numbers.
# Find and print the max element and the index of this element.

# Example: [1, 45, 33, 76, 9, 10], print [3, 76]


# 0(n)
# def find_max_item(arr):
#     max_num = arr[0]
#     max_index = 0
#
#     for i in range(1, len(arr)):
#         if arr[i] > max_num:
#             max_num = arr[i]
#             max_index = i
#
#     print([max_index, max_num])
#
# test_list = [1, 45, 33, 76, 9, 10]
# find_max_item(test_list)