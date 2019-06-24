import random

list1=[]
for i in range(0, 101):
    list1.append(i)
result = random.choice(list1)
print(result)