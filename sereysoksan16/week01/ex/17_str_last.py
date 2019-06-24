input_string = input('Enter a string: ')
string_length = len(input_string)
if string_length > 0:
    new = input_string[-1]
    print(new)
else:
    print('Empty')
