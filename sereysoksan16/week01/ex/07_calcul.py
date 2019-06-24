result = 0
while 1:
    input_number = input('Enter a number: ')
    try:
        # if the value is number
        # is digit is not support with negative value
        integer_number = int(input_number)
        result = result+integer_number
        print('TOTAL: ' + str(result))
    except ValueError:
        # if the value is not number
        if input_number == 'exit':
            quit()
        else:
            print('TOTAL: ' + str(result))
