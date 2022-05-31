 # Compute the sum of digits in all numbers form 1 to n
# When a user enters a number n, find the sum from 1 to n
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
# Exercise # 1

# 0 (n)
# n = int(input('Please enter a number from 1 to any number: '))
# print(f'The number n is: {n}')
#
#
# def sum_of_list(n):
#   total = 0
#   for val in range(1, n +1):
#     total = total + val
#   return total
#
#
# print("The sum of my_list is", sum_of_list(n))

# Exercise # 2
# Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124

# 0(1)
# a = int(input("Enter First number: "))
# b = int(input("Enter Second number: "))
# c = int(input("Enter Third number: "))
#
#
# def maximum(a, b, c):
#     if (a >= b) and (a >= c):
#         largest = a
#     elif (b >= a) and (b >= c):
#         largest = b
#     else:
#         largest = c
#     return largest
#
# print(maximum(a, b, c))


# Exercise # 3
# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6 and 0) and 2 odd digits (3 and 5)

# number = int(input('Please, enter a number: '))

# 0(n)

# possible solution
# oddcount = number//100%2 + number//10%10%2 + number%10%2    # this exercise if for 3-digit number
# if oddcount==3:
# 	print("All are odd")
# elif oddcount==0:
# 	print("All are even")
# else:
# 	print("Mixed")


# possible solution
# if(number%2==0):      # this exercise if for the number itself, not digits
#    print('number is even')
# else:
#    print('number is odd')

# 0(n)
# def count_odd_even(n):
#     odds = []
#     evens = []
#
#     while n != 0:
#         current_digit = n % 10
#         if current_digit % 2:
#              odds.append(current_digit)
#         else:
#             evens.append(current_digit)
#         n = n // 10
#
#     return ['Evens : ' + str(evens), 'Odds: ' + str(odds)]
#
#
# print(count_odd_even(34568))
#
