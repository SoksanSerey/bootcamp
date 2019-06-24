def current_time():
    import datetime

    # this function is written to print the current time with the format: hh:mm:ss
    x = datetime.datetime.now()
    result = x.strftime("%H:%M:%S")
    # format the time string into hh:mm:ss
    return result


# print(current_time())
