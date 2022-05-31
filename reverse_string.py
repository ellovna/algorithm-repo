# Code challenge #4
# Given a string. Return a reversed string
# For example, abcde -> edcba.

# 0(n)
def reverse_string(s):
    reversed_s = ''
    index = len(s) - 1
    while index >= 0:
        reversed_s += s[index]
        index -= 1

    return reversed_s

test_s = 'abcde'
print(reverse_string(test_s))