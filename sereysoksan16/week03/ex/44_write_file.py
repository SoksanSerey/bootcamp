"""
You will write a function that take two arguments: The first argument is a filename, the second is the content.
Your program will create a new file inside the current directory with the name you specify. Then it will write the
content you specify in the second argument. Finally your program will close the file and return 1
If you try to replace a file that already exist, you will ask confirmation of the user :
“Are you sure you want to replace <FILENAME>? [Y/N]”
If the user write Y, you will create the new file and return 1
If the user write N, you will just return 0
If the user write anything else, you will print :
“Invalid Option” and then print the confirmation message again:
“Are you sure you want to replace <FILENAME>? [Y/N]”
"""


def write_file(file_name, content):
    import os

    def check_existed(file, cont):
        """
        confirmation of writing the
        :param file: path that we need to check
        :param cont: content that we need to write
        :return: 1 if the file is write and 0 if don't do anything to the file
        """
        cond_check = True
        while cond_check:
            inp_string = input('“Are you sure you want to replace ' + file + '? [Y/N]\n')
            if inp_string == 'Y':
                rewrite_file(file, cont)
                return 1
            elif inp_string == 'N':
                return '0'
            else:
                print('Invalid Option')
                cond_check = True
                continue

    def rewrite_file(file, cont):
        """
        Write the content into the path
        :param file: name of the file
        :param cont: content that we are going to write
        :return: return 1 after write the file
        """
        f = open(file, 'w')
        f.write(cont)
        f.close()
        return 1

    exists = os.path.isfile(file_name)
    if exists:
        # check whether the path exist or not
        re_va = check_existed(file_name, content)
        return re_va
    else:
        rewrite_file(file_name, content)
        return 1


# print(write_file('./test/hello', 'This is the content of hello file'))
