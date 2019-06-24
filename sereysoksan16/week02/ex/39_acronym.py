def acronym(list1):
    # this function will take a list as parameter
    new_list = []
    for i in range(0, len(list1)):
        x = list1[i][0]
        # this will take the first character of the list item
        y = x.upper()
        # convert it into uppercase
        new_list.append(y)
        # add it into a new list
    return new_list


# ran_list = ['world', 'wide', 'web', 'hell']
# print(acronym(ran_list))
