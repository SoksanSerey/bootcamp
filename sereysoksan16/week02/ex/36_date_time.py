def date_time():
    import datetime

    # this function will return the current date and time with the format of YYYY-MM-DD hh:mm:ss
    x = datetime.datetime.now()
    result = x.strftime("%Y-%m-%d %H:%M:%S")
    # this code is to format the string of date
    return result


# print(date_time())
