"""
You will create a function that detect if string contains only value from a-z A-Z and 0-9.
You function will take one argument in parameter ( a string ) and will return True or False ( boolean )
If the string in empty, you will return False
"""


def regex_alpha(input_string):
    import re

    if len(input_string) > 0:
        if re.match('^[A-Za-z0-9]*$', input_string):
            # if the string contain only A-Z, a-z and 0-9
            return True
        else:
            return False
    else:
        return False


# print(regex_alpha('fajadfj323'))
