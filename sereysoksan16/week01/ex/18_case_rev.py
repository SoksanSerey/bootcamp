input_string = input('Enter a string: ')
str_len = len(input_string)
if str_len > 0:
    for i in range(0, str_len):
        if 90 >= ord(input_string[i]) >= 65:
            print(chr(ord(input_string[i]) + 32), end="")
            # this code is to convert all the capital character into a small character
        elif 122 >= ord(input_string[i]) >= 97:
            print(chr(ord(input_string[i]) - 32), end="")
            # this code is to convert small character into capital character
        else:
            print(input_string[i], end="")
            # all the special symbol and number will remain the same
else:
    print('Empty')
