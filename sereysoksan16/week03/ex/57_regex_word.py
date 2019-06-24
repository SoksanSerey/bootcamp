"""
You will create a function that remove all words from a string length of between 1 and give number. This function will
take one integer in parameter that represent the length and one string that represent the text to be formatted.
You need to return the new string. If the number is negative or 0 you will return an empty string. The special
characters will not be removed.
"""


def regex_word(input_int, input_string):
    import re

    result = re.compile(r'\W*\b\w{1,' + str(input_int) + r'}\b')
    # used to remove all the string that have less than the input string and won't remove the special character
    result = result.sub('', input_string)
    return result


# print(regex_word(3, 'My name is Soksan?'))
