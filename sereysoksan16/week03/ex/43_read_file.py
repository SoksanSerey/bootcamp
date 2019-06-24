"""
You will write a function that take a filename as argument (string). The filename represent the name of the file your
program will read. First you will make sure that the file exist, then you will print the content and finally you will
return the value as string. If the file is not valid ( folder ) or doesn’t exist :
You will print ‘Invalid FILENAME’ Then, you will return an empty string.
"""


def read_file(file_name):
    output_string = ''
    try:
        # if the path exist
        f = open(file_name, 'r')
        output_string = f.read()
        f.close()
        return output_string
    except FileNotFoundError:
        # if the path doesn't exist
        print('Invalid FILENAME')
        return output_string


# print(read_file('./test/hello'))
