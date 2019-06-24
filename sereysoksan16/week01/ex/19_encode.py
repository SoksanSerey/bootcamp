input_string = input('Enter your secret message: ')
str_len = len(input_string)
if str_len > 0:
    for i in range(0, str_len):
        if (65 <= ord(input_string[i]) <= 77) or \
                (97 <= ord(input_string[i]) <= 109):
            # the character between A to M and a to m will go into this condition
            print(chr(ord(input_string[i]) + 13), end="")
        elif (0 <= ord(input_string[i]) <= 64) or \
                (91 <= ord(input_string[i]) <= 96) or \
                (123 <= ord(input_string[i]) <= 127):
            print(chr(ord(input_string[i])), end="")
            # this condition is used to avoid all the special character and number to be converted
        else:
            print(chr(ord(input_string[i]) - 13), end="")
            # the character between N to Z and n to z will be in this condition
else:
    print('Nothing to encode.')
