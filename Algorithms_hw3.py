
# Exercise# 1 Below the Arithmetical Mean

# When given a list, the program should return a list of all the elements below the original
# list's arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

# I didn't know how to return a list of all the elements below the original list's arithmetical mean.
# Just found the arithmetical mean:

list = [1, 3, 5, 6, 4, 10, 2, 3]
Sum = sum(list)
a_mean = Sum / len(list)

print(a_mean)


# Exercise #2 Two lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

list = [198, 3, 4, 9, 10, 9, 2]
list.sort()

print("Smallest element is:", *list[:2])



