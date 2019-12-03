import random
import matplotlib.pyplot as plt


def monte_carlo(x):
    size = ['S', 'M', 'L']
    list1 = []
    list2 = [1, 2, 3]
    list_size = []
    list_occ = []
    for i in range(0, int(x)):
        y = random.choice(size)
        list1.append(y)
    dict1 = {}
    for letter in set(list1):
        amount = list1.count(letter)
        dict1[letter] = amount
    for key in dict1.keys():
        list_size.append(key)
    for value in dict1.values():
        list_occ.append(value)
    plt.bar(list2, list_occ, tick_label=list_size, width=0.8, color=['blue', 'green', 'red'])
    plt.xlabel('T-shirt size')
    plt.ylabel('Amount of T-shirt')
    plt.title('Random T-shirt chosen')
    plt.show()
    # print(list_size)
    # print(list_occ)
    return list1


while True:
    student = input("Insert number of student you want to random T-shirt size for: ")
    if student.isdigit() and int(student) > 0:
        print(monte_carlo(student))
    else:
        print("Student should be in positive number and not 0")
        continue
    break
