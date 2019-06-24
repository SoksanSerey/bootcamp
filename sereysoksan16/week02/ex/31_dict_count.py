def dict_count(list1):
    # this function will take a list as parameter
    # [[x, list1.count(x)] for x in set(list1)]
    # new_dict = dict((x, list1.count(x)) for x in set(list1))  # list comprehension function
    new_dict = {}
    for letter in set(list1):
        amount = list1.count(letter)
        new_dict[letter] = amount
        # this will add the element of list as key in dict and occurrence of it as value
    return new_dict


# ran_list = ['a', 'a', 'a', 'b', 'c', 'd', 'c', 'b', 'c', 'd', 'c', 'e', 'e', 'e', 'f', 'f', 'z']
# print(dict_count(ran_list))
