
# Find a sum of elements between min and max elements.
# Min and max elements are not included
# All numbers are unique.

# 0(N)
# def sum_between_min_and_max(arr):
#     if len(arr) < 2:
#         return 0
#
#     min_item = max_item = arr[0]
#     min_index = max_index = i = 0
#
#     while i < len(arr):
#         if arr[i] > max_item:
#             max_item = arr[i]
#             max_index = i
#         if arr[i] < min_item:
#             min_item = arr[i]
#             min_index = i
#         i += 1
#
#     return sum(arr[min(min_index, max_index) + 1:max(min_index, max_index)])
#
#
# test_list_1 = [4, 2, 3, 6, 8, 9, 11, 7]  # min item 2, max_item 11
# test_list_2 = [40, 3, 2, 6, 8, 9, 11, 7]  # min_item = 2, max_item = 40
#
# print(sum_between_min_and_max(test_list_1))
# print(sum_between_min_and_max(test_list_2))
