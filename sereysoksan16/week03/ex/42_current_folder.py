"""
You will write a function that return a tuple list with all files and folders inside the current path. For each tuple,
the first value will be the file or folder name. The second value will be the kind of file (‘Folder’ or ‘File’).
"""


def current_folder():
    import os

    new_list = []
    for root, dirs, files in os.walk('.'):
        # os.walk will split the value into 3: 1st is root, 2nd is directory and 3rd is file
        for folder in dirs:
            # loop the content that from the directory generate by os.walk
            temp_tuple = (folder, 'Folder')
            new_list.append(temp_tuple)
        for file in files:
            # loop the file that from the files generate by os.walk
            temp_tuple = (file, 'File')
            new_list.append(temp_tuple)
    return sorted(new_list, key=lambda x: x[0])


# cont = current_folder()
# print(cont)
