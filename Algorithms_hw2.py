# HW1
# Split in Half
# Given a string. Split into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example, string = 'bbbbbcaaaaa'. Result = 'aaaaabbbbbc'
#
# text = 'bbbbbcaaaaa'
#
# str_1 = text[:len(text)//2]
# str_2 = text[len(text)//2:]

# print(str_1, str_2)
#
# if len(str_1) % 2 == 0:
#     print('Characters are even')
# else:
#     print('aaaaabbbbbc')

# 0(1)
# def split_in_half(s):
#     length = len(s)
#     half = length // 2
#     add = 0
#
#     if length % 2:
#         add = 1
#
#     left = s[:half + add]
#     right = s[half + add:]
#     print(f'left = {left}')
#     print(f'right = {right}')
#
#     print(right + left)
#
# test_data_even = 'aaaccc'
# test_data_odd = 'aaabccc'
# split_in_half(test_data_odd)
# split_in_half(test_data_even)
#


# HW2
# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

# word = 'aabcde'
# unique_characters = ""
#
# for character in word:
#     if character not in unique_characters:
#         unique_characters += character.lower()
#
# print('The list of unique characters is: {}'.format(unique_characters))
# print("False")

# def uni_char(s):
#     return len(set(s)) == len(s)

# 0(n)
# def uni_char(s):
#     chars = set()
#
#     for let in s:
#         if let in chars:
#             return False
#         chars.add(let)
#
#     return True
#
#
# test_data_all_uni = 'abcde'
# test_data_dup = 'abcdd'
#
# print(uni_char(test_data_all_uni))
# print(uni_char(test_data_dup))
#
