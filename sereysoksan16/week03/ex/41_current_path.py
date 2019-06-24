"""
You will write a function that print the current path of your program folder, then you will return it as a string.
"""


def current_path():
    import os

    dir_path = os.getcwd()
    return dir_path


# print(current_path())
