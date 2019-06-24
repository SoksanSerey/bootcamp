num1 = int(input('Enter the first number: \n'))
num2 = int(input('Enter the second number: \n'))

if num1 < num2:
    print('Result : ' + str(num1)+' < '+str(num2))
elif num2 < num1:
    print('Result : ' + str(num2)+' < '+str(num1))
else:
    print('Result : ' + str(num1)+' == '+str(num2))
