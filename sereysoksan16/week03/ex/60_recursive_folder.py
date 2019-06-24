"""
You will write a function that take a string in parameter that represent a given path and return files path recursively.
The paths must be sorted. If the folder is empty, you must not display it. Also, don’t display your program name.
"""


def recursive_folder(path):
    import os

    list_dir = []
    try:
        # if the path is correct
        for roots, dirs, files in os.walk(path):
            for file in files:
                list_dir.append(os.path.join(roots, file))
        return list_dir
    except Exception:
        # if the path is incorrect
        return list_dir


# print(recursive_folder('.'))
