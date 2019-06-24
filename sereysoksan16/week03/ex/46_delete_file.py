"""
You will create a function that has the power to delete any file or any folder that is specify. Your function will take
one parameter (filename) that can be a Folder or a File. Then, the function will ask for confirmation:
“Are you sure you want to delete <FILENAME>? [Y/N]”
If the user write anything that is not Y or N you will print:
“Invalid Option” and then print the confirmation message again:
“Are you sure you want to delete <FILENAME>? [Y/N]”
If a file has been deleted, your function will return 1, else return 0.
"""


def delete_file(file_name):
    import os
    import shutil

    exist = os.path.exists(file_name)  # check whether the path exist
    file = os.path.isfile(file_name)  # check whether the path is file
    folder = os.path.isdir(file_name)  # check whether the path is folder
    if exist:
        cond_check = True
        while cond_check:
            input_string = input('Are you sure want to delete ' + file_name + '? [Y/N]\n')
            if input_string == 'Y':
                if file:
                    os.remove(file_name)  # remove the file
                elif folder:
                    shutil.rmtree(file_name)  # remove the folder and everything inside
                return 1
            elif input_string == 'N':
                return 0
            else:
                print('Invalid Option')
                continue
    else:
        return 0


# print(delete_file('c'))
