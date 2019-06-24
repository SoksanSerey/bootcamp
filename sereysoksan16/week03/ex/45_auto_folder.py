"""
You will create a program that take a list of string as argument, that represents folders names. Then, for each, you
will create a folder with the corresponding name. Before create anything, you will check that the folders doesn’t
already exists. If they, you will ask:
“Are you sure you want to replace <FOLDER_NAME>? [Y/N]”
If the user enter anything that is not Y or N, you will write:
“Invalid Option” and then print the confirmation message again:
“Are you sure you want to replace <FOLDER_NAME>? [Y/N]”
Make sure that you ask for EVERY folders that already exist only.
"""


def auto_folder(list01):
    import os

    def check_existed(folder):
        """
        confirmation after the folder is exist, whether we want to replace or else
        :param folder: list of folder we want to create
        :return: 1 if any new folder created and 0 if not
        """
        cond_check = True
        while cond_check:
            input_option = input('Are you sure you want to replace ' + folder + '? [Y/N]\n')
            if input_option == 'Y':
                os.rmdir(folder)
                create_folder(folder)
                return 1
            elif input_option == 'N':
                return 0
            else:
                print('Invalid Option')
                continue

    def create_folder(folder):
        """
        Create the folder
        :param folder: folder name
        :return: 1 after create folder
        """
        os.mkdir(folder)
        return 1

    if len(list01) > 0:
        for i in list01:
            exist = os.path.exists(i)
            if exist:
                res = check_existed(i)
            else:
                res = create_folder(i)
            res += res
        if res > 1:
            return 1
        else:
            return 0
    else:
        return list01


# print(auto_folder(['a', 'b', 'c']))
