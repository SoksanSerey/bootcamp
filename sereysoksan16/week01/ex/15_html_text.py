i = 0
list1 = []
while 1:
    input_string = input('Enter a string: ')
    if input_string == 'Generate':
        num = len(list1)
        for i in range(0, num):
            new_string_len = len(list1[i])
            print('<p>', end="")
            for j in range(0, new_string_len):
                if (90 >= ord(list1[i][j]) >= 65) or (122 >= ord(list1[i][j]) >= 97):
                    print(list1[i][j], end="")
                    # this condition is to rewrite all the alphabet into the title and avoid all the special character
                elif ord(list1[i][j]) == 32:
                    print(list1[i][j], end="")
                    # this condition is to allow the space to be use in the title
                else:
                    continue
                    # this is all the ignore character will come here
            print('</p>')
        quit()
    else:
        list1.append(input_string)

