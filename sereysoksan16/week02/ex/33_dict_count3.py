def dict_count3(list1):
    # this function will take a list as parameter
    new_list = []
    total = 0
    for letter in set(list1):
        amount = list1.count(letter)
        # this above code is to count the occurrence of the each element in list
        new_tuple = (letter, amount)
        # this code is to write a tuple that take element as first value and amount as second value
        total += amount
        new_list.append(new_tuple)
        # this code is add the tuple as items in list
    if total > 0:  # check whether the input has value or not
        print('TOTAL:', total)
    else:
        print('Your string is empty.')
    another_list = sorted(new_list, key=lambda x: x[0])
    # the above code will sort the list by the first value of the tuple inside that list using lambda function
    return another_list


# ran_list = ['a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'e', 'e', 'e']
# print(dict_count3(ran_list))
