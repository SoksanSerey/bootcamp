def list_sort_int(list1):
    # this function will take the a list in parameters
    new_list = list()
    for i in range(0, len(list1)):
        if list1[i].isdigit():
            new_list.append(int(list1[i]))
            # this condition will check the value of the list is digit or not and will add digit as integer to new list
        else:
            continue
            # this condition will ignore the list value that not digit
    return sorted(set(new_list))


# ran_list = ['abc', '4', '4', '4', '4', '2', '3', 'dza', 'def']
# print(list_sort_int(ran_list))
