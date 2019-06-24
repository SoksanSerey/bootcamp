# this function will take a string as parameter
def top_words(text):
    import re
    import string

    count = dict()
    another_dict = {}
    list01 = []
    list02 = []
    # convert the whole string into the lowercase
    y = text.lower()
    # remove punctuation from the string
    remove_pun = string.punctuation
    remove_pun = remove_pun.replace("'", "")
    pattern = r"[{}]".format(remove_pun)
    x = re.sub(pattern, "", y)
    # remove digit from the string
    remove_digit = string.digits
    pattern2 = r"[{}]".format(remove_digit)
    z = re.sub(pattern2, "", x).split()
    # count each occurrence and put it into the string
    for word in z: 
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    # sort dict by value
    for key, value in sorted(count.items(), key=lambda item: item[1], reverse=True):
        another_dict[key] = value
    # insert key of dict into list
    for key in another_dict.keys():
        list01.append(key)
    # print the 
    if len(list01) <= 3:
        return list01
    else:
        for i in range(0, 3):
            list02.append(list01[i])
        return list02


# ran_str = input('Enter any string: ')
# print(top_words(ran_str))
