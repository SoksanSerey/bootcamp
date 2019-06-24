def list_sort_str(list1):
    # this function will take a list as parameter
    new_list = list()
    for i in range(0, len(list1)):
        if list1[i].isdigit():
            continue
            # this will check, if the list items is number, it will ignore that
        else:
            new_list.append(list1[i])
            # this will take the value that not number and add it into a new list
    return sorted(new_list)
    # it will sorted the new list and return it


# ran_list = ['abc', '4', '2', '3', 'dza', 'def']
# print(list_sort_str(ran_list))
