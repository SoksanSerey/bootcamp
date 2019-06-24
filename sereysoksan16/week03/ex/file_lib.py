"""
this class is used to contain all the method form exercise 41 to 47
"""


class FileLib:
    def current_path(self):
        """
        This method is used to find the current path
        :return: current directory
        """
        import os
        
        dir_path = os.getcwd()
        return dir_path
    
    def inspect(self):
        """
        this method is used to write the file and folder and display it as in tuple
        :return:
        """
        import os

        new_list = []
        for root, dirs, files in os.walk('.'):
            for folder in dirs:
                temp_tuple = (folder, 'Folder')
                new_list.append(temp_tuple)
            for file in files:
                temp_tuple = (file, 'File')
                new_list.append(temp_tuple)
        return sorted(new_list, key=lambda x: x[0])

    def read(self, file_name):
        """
        This method is used to read the content inside the file
        :param file_name: file name that we want to read
        :return: output in that file we read as string
        """
        output_string = ''
        try:
            f = open(file_name, 'r')
            print(f.read())
            output_string = f.read()
            f.close()
            return output_string
        except FileNotFoundError:
            print('Invalid FILENAME')
            return output_string

    def write(self, file_name, content):
        """
        This method is used to write the content into the specific file name that we receive
        :param file_name: path of the file that we want to write to
        :param content: what we want to add into the file
        :return: return 1 if it is success and 0 is it fail
        """
        import os

        def check_exist(file, cont):
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
            f = open(file, 'w')
            f.write(cont)
            f.close()
            return 1

        exists = os.path.isfile(file_name)
        if exists:
            re_va = check_exist(file_name, content)
            return re_va
        else:
            rewrite_file(file_name, content)
            return 1
    
    def create_folder(self, list01):
        """
        this method is used to get a list that contain name of folder and create that folder is not yet exist
        :param list01: list that contain folder name
        :return: return 0 if it fail and 1 if it success
        """
        import os

        def check_exist(folder):
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
            os.mkdir(folder)
            return 1

        if len(list01) > 0:
            for i in list01:
                exist = os.path.exists(i)
                if exist:
                    res = check_exist(i)
                else:
                    res = create_folder(i)
                res += res
            if res > 1:
                return 1
            else:
                return 0
        else:
            return list01

    def remove(self, file_name):
        """
        This method is used to remove the file or folder that we insert as param
        :param file_name: name of file or folder we want to delete
        :return: return 1 if it success and 0 if it fail
        """
        import os
        import shutil

        exist = os.path.exists(file_name)
        file = os.path.isfile(file_name)
        folder = os.path.isdir(file_name)
        if exist:
            cond_check = True
            while cond_check:
                input_string = input('Are you sure want to delete ' + file_name + '? [Y/N]\n')
                if input_string == 'Y':
                    if file:
                        os.remove(file_name)
                    elif folder:
                        shutil.rmtree(file_name)
                    return 1
                elif input_string == 'N':
                    return 0
                else:
                    print('Invalid Option')
                    continue
        else:
            return 0

    def append(self, file_name, content):
        """
        This method is used to append the content into the file
        :param file_name:
        :param content:
        :return:
        """
        f = open(file_name, 'a+')
        f.write(content)
        f.close()
