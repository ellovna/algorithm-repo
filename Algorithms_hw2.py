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


# HW2
# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

word = 'aabcde'
unique_characters = ""

for character in word:
    if character not in unique_characters:
        unique_characters += character.lower()

print('The list of unique characters is: {}'.format(unique_characters))
print("False")

