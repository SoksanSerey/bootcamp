def time_list(int_value):
    import datetime

    # this function will ake one integer as parameter
    list1 = []
    int_value = str(int_value)
    if int_value.isdigit():
        # this condition will check the input is valid or not
        current_datetime = datetime.datetime.now()
        for i in range(0, int(int_value)):
            new_time = current_datetime + datetime.timedelta(seconds=i)
            # the above code will take the current time and add 1 second
            a = new_time.strftime("%H:%M:%S")
            list1.append(a)
            # it will add the current time to the list equal to the input integer time
    else:
        # if the input is invalid it will come here
        print('Invalid integer.')
    return list1


# ran_value = input('Enter a integer: ')
# print(time_list('10'))
