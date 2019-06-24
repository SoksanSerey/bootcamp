def timestamp_to_str(input_timestamp):
    import datetime

    input_timestamp = str(input_timestamp)
    # this function will take the timestamp string as input
    try:
        # this condition will check whether the input is valid or not
        input_timestamp = int(input_timestamp)
        result = datetime.datetime.utcfromtimestamp(input_timestamp)
        result = result + datetime.timedelta(hours=7)
        # the above code will convert the timestamp into readable date
        return result
    except (ValueError, OSError):
        # if the input is invalid, it will come here
        result = 'Your timestamp is not valid'
        print(result)
        return 0
    # return result


# ran_timestamp = input('Enter a timestamp: ')
print(timestamp_to_str(-1))
