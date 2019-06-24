while 1:
    number = input('Enter a number: \n')
    if number.isdigit():
        num1 = int(number)
        if num1 % 2 == 0:
            print(str(num1) + ' is EVEN')
        elif num1 % 2 != 0:
            print(str(num1) + ' is ODD')
        # print('sth')
    elif number == 'exit' or number == 'EXIT':
        quit()
    else:
        print(number + ' is not a valid number.')
