import random

list1 = []
for i in range(0, 101):
    list1.append(i)
number = int(input('Enter a number: '))
for i in range(0, number):
    result = random.choice(list1)
    print(result)
