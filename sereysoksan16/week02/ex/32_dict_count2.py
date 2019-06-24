def dict_count2(list1):

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

    # check whether the input has value or not
    if total > 0:
        print('TOTAL:', total)
    else:
        print('Your string is empty.')
    another_list = sorted(new_list, key=lambda x: (-x[1], x[0]))
    # the above code will sort the list by the second value of the tuple inside that list using lambda function

    return another_list


# ran_list = ['z', 'z', 'z', 'z', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c', 'c']
# print(dict_count2(ran_list))
