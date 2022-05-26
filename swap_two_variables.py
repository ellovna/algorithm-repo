# User inputs two numbers. One number is assigned to a variable, the other number is assigned to another variable.
# The task is to invert the variables, so that the first variable contains the second number, while the first number
# is in the second variable.

# 0(1)
# a = int(input('Input value a: '))
# b = int(input('Input value b: '))

# print(f'a = {a}, b = {b}')

# temp = a
# a = b
# b = temp

# a, b = b, a

a = a + b
b = a - b
a = a - b

# print(f'a = {a}, b = {b}')