# 1. Even First
# Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input array)
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
#
# array = [7, 3, 5, 6, 4, 10, 3, 2]
#
# even = []
# odd = []
#
# for value in sorted(array):
#     if value % 2 == 0:
#         even.append(value)
#     else:
#         odd.append(value)
#
# combined = even + odd
#
# print(*combined)


# 2 Increment a Number
# Write a program that takes as input an array of digits encoding a non negative decimal integer D and updates
# the array to represent the integer D + 1
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0]
#
# D = [1, 2, 3]
# for i in range(len(D)):
#     D[i] += 1
#
# print(D)    # It gave me different number [2, 3, 4]