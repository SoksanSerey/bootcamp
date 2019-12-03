def decode(x):
    """
    This function is used to decode the caesar cipher algorithm by brute force and get all possible answer
    :param x: cipher text
    :return: dictionary of all possible answer
    """
    dict1 = {}
    if len(x) > 0:
        for i in range(0, 26):
            result = ""
            for j in range(0, len(x)):
                if x[j].isupper():
                    result += chr((ord(x[j]) - i - 65) % 26 + 65)
                elif (0 <= ord(x[j]) <= 64) or \
                        (91 <= ord(x[j]) <= 96) or \
                        (123 <= ord(x[j]) <= 127):
                    result += chr(ord(x[j]))
                else:
                    result += chr((ord(x[j]) - i - 97) % 26 + 97)
            dict1[i] = result
    else:
        print("No message to decode")
    return dict1


cipher_text = input("Enter cipher text to encrypt: ")
print(decode(cipher_text))
