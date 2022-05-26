# Our code generates a random three-digit number and has to sum up all its digits.
# For example, if a number is 349, the code has to print the number 16, because 3 + 4 + 9 = 16.

from random import randint

# random_number = randint(100, 999)
# print(f'The random number is: {random_number}')

# result = 0
# # for digit in str(random_number): # 347 - [3, 4, 9]
# #     result = result + int(digit)
#
# # 0(n) # n = length of random_number
# while random_number != 0:
#     result = result + (random_number % 10)
#     random_number = random_number // 10
#
# print(f'Result: {result}')
