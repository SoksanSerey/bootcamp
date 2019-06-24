"""
You will create a function that take a string in parameter and remove every HTML content ( everything between
‘<’ and ‘>’ ) You will return the new formatted string.
"""


def regex_html(input_str):
    import re

    result = re.sub(r'\<[^>]*\>', '', input_str)
    # regex function that will remove anything inside <>
    return result


# print(regex_html("<html lang = 'pl' ><body> content of body </body> ... </html>"))
