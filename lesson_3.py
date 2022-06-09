# Ex #1 Find the missing element

# Consider an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which element is missing in the second array.
# Here is an example input, the first arrays is shuffled and the number 5 is removed to construct the second array.

# Input: [1,2,3,4,5,6,7],[3,7,2,1,4,6]
# Output: 5 is the missing number

# 0(0n)
# def find_missing_number(arr1, arr2):
#     arr1.sort()
#     arr2.sort()
#
#     for num1, num2 in zip(arr1, arr2):
#         if num1 != num2:
#             return num1
#
#     return arr1[-1]
#
# import collections
#
# # 0(N)
# def find_missing_number(arr1, arr2):
#     d = collections.defaultdict(int)
#
#     for num in arr2:
#         d[num] += 1
#
#     for num in arr1:
#         if d[num] == 0:
#             return num
#         else:
#             d[num] -= 1
#
#
#
# test_arr1 = [1, 2, 3, 4, 5, 6, 7]
# test_arr2 = [3, 7, 2, 1, 4, 6]
#
# print(find_missing_number(test_arr1, test_arr2))

# Ex # 2 Largest Continuous Sum

# Given an array of integers (positive or negative) find the largest continuous sum.

# Input:[1,2,-1,3,4,10,10-10,-1]
# Output:[29(1+2+-1+3+4+10+10=29]

# 0(n)
# def find_sum(arr):
#     if len(arr) == 0:
#         return 0
#
#     max_sum = arr[0]
#     current_sum = arr[0]
#
#     for num in arr[1:]:
#         current_sum = max(current_sum + num, num)
#         max_sum = max(current_sum, max_sum)
#
#     print(max_sum)
#
# test_data = [1, 2, -1, 3, 4, 10, 10, -10, -1]
# find_sum(test_data)



# Ex # 3 - Mountain array

# Given an array of integers, return if the following conditions are fulfilled:
# - length of the array is bigger than or equal to 3
# - there exists some index i such that:
# a[0] < a[i]
# a[i] > a[i+1] > a[a.size-1]

# Basically, find if there is an increasing subarray followed by decreasing subarray
# [3,5,5] -> false
# [3,4,5,2] -> true

# 0(n)
# def is_mountain(array):
#     if len(array) < 3:
#         return False
#
#     i = 1
#     while i < len(array) and array[i] > array[i - 1]:
#         i += 1
#     if i == 1 or i == len(array):
#         return False
#     while i < len(array) and array[i] < array[i - 1]:
#         i += 1
#
#     return i == len(array)
#
# test_data_positive = [1, 4, 7, 9, 5, 2]
# test_data_negative = [1, 4, 7, 9, 5, 6]
#
# print(is_mountain(test_data_positive))
# print(is_mountain(test_data_negative))


# def print_numbers(arr):
#     for num in arr[1:]:
#         print(num)
#
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print_numbers(array)
#
# my_first_list = [1, 5, 7, 9]
# my_second_list = [-5, 643]


# my_first_list.append(25)
# print(my_first_list)
# my_first_list.clear()
# print(my_first_list)
# print(my_first_list.count(5))
# print(my_first_list.index(5))
# my_first_list.insert(0, 99)
# my_first_list.pop(my_first_list.index(5))
# my_first_list.remove(7)
# # my_first_list.reverse()
# my_first_list.sort()
# print(my_first_list)


# Ex # 4
# 0(N)
# Given an array of integers, write a function to move all 0's to the end while maintaining the relative order of the other elements.

# Input:0 4 03 12
# Output: 4 3 12 0

# def move_zeroes(arr):
#     j = 0
#
#     for num in arr:
#         if num != 0:
#             arr[j] = num
#             j += 1
#
#     while j < len(arr):
#         arr[j] = 0
#         j += 1
#
#     return arr
#
# test_data = [0, 4, 0, 3, 12]
# print(move_zeroes(test_data))


# Ex # 5 Two sums

# Given an array of integers nums and an integer target.
# Return two numbers from the array such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input:[3,7,4,9,15,3],6
# Output: 3,3

# def pait_sum(arr, k):
#     if len(arr) < 2:
#         return
#
#     sum_set = set()
#
#     for num in arr:
#         target_value = k - num
#         if target_value not in sum_set:
#             sum_set.add(num)
#         else:
#             return(target_value, num)
#
# test_data = [3,7,4,9,15,3]
# test_target = 6
#
# print(pait_sum(test_data, test_target))


