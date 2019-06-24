"""
You need to create a function that take a string in parameters and return a string without any parenthesis content.
"""


def regex_par(input_str):
    import re

    result = re.sub(r'\([^()]*\)', '', input_str)
    # regex function that used to select string that don't have any parenthesis content
    return result


# print(regex_par("(hello) Welcome to KIT (Kirirom Institute of Technology)!"))
