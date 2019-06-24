def append_file(file_name):
    """
    this function is used to append the content to the file that include the datetime of when it insert
    :param file_name: path of the file
    """
    from datetime import datetime

    cond_check = True
    while cond_check:
        user_input = input('$: ')
        x = datetime.now()
        date_time = x.strftime('%d/%m/%Y %H:%M:%S')
        if user_input == 'EXIT':
            cond_check = False
        else:
            file = open(file_name, 'a+')
            file.write('[' + date_time + '] ' + user_input + '\n')
            file.close()


# append_file('.//test//hello')
