number = input('Enter a number: \n')
if number.isdigit():
    num = int(number)
    for i in range(0, num):
        print('Hello world!')
else:
    print('Nothing to display')
