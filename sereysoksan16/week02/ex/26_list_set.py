def list_set(list1):
    # this function will take a list as parameter and return a list with unique value only
    list2 = []
    list1 = set(list1)
    for i in list1:
        list2.append(i)
    return list2


# ran_list = ['456', '123', '789', '123', 'abc', 'abc', 'def']
# print(list_set(['456', '123', '789', '123']))
