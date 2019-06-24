input_string = input('Enter a title: ')
string_length = len(input_string)
if string_length > 0:
    print('<h1>', end="")
    for i in range(0, string_length):
        if (90 >= ord(input_string[i]) >= 65) or \
                (122 >= ord(input_string[i]) >= 97):
            print(input_string[i], end="")
            # this condition is to rewrite all the alphabet into the title and avoid all the special character
        elif ord(input_string[i]) == 32:
            print(input_string[i], end="")
            # this condition is to allow the space to be use in the title
        else:
            continue
            # this is all the ignore character will come here
    print('</h1>')
else:
    print('This is empty.')
