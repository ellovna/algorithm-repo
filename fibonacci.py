# The task is to display all the numbers from start to n of the Fibonacci sequence


# Equation:
# F0 = 0
# F1 = 1
# F2 = 1
# F3 = Fn-1 + Fn-2

#  1 1 2 3 5 8 13 ...

fib_number = int(input("Provide a number: "))

index = 3
fib_1 = 1
fib_2 = 1
result = [fib_1, fib_2]

# 0(n)
while index <= fib_number:
    result.append(fib_1 + fib_2)
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    index = index + 1  # index += 1

print(result)



