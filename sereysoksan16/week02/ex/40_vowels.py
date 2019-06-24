def vowels(input_string):
    # this function will take a string as input
    count = 0
    can_vow = ''
    can_string = ''
    for i in range(0, len(input_string)):
        if input_string[i] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            # this condition will check whether the character is vowel or not
            count += 1
            can_vow = can_vow + input_string[i].lower()
            # this will covert the vowel into lower case and concatenate it together
        elif ord(input_string[i]) == 32:
            continue
            # this cond
        else:
            can_string = can_string + input_string[i].upper()
    if count > 0:
        # print(count)
        print(can_vow)
        print(can_string)
    else:
        print('NO VOWELS')
    return count


# ran_string = 'What is that?'
# print(vowels(ran_string))
