def encrypt(x, y):
    """
    This function is written to encrypt the message for the user
    :param x: plaintext
    :param y: key
    :return: cipher text
    """
    user_key = int(y)
    result = ""
    plaintext_len = len(x)
    if plaintext_len > 0:
        for i in range(0, plaintext_len):
            if x[i].isupper():
                result += chr((ord(x[i]) + user_key - 65) % 26 + 65)
            elif (0 <= ord(x[i]) <= 64) or \
                    (91 <= ord(x[i]) <= 96) or \
                    (123 <= ord(x[i]) <= 127):
                result += chr(ord(x[i]))
            else:
                result += chr((ord(x[i]) + user_key - 97) % 26 + 97)
    else:
        print("Nothing to encrypt")
    return result


def decrypt(x, y):
    """
    This function is written to decrypt the message for the user
    :param x: plaintext
    :param y: key
    :return: cipher text
    """
    user_key = int(y)
    result = ""
    if len(x) > 0:
        for i in range(0, len(x)):
            if x[i].isupper():
                result += chr((ord(x[i]) - user_key - 65) % 26 + 65)
            elif (0 <= ord(x[i]) <= 64) or \
                    (91 <= ord(x[i]) <= 96) or \
                    (123 <= ord(x[i]) <= 127):
                result += chr(ord(x[i]))
            else:
                result += chr((ord(x[i]) - user_key - 97) % 26 + 97)
    else:
        print("Nothing to encrypt")
    return result


while True:
    key = input("Enter key: ")
    try:
        while True:
            choice = int(input("Enter 1 to encrypt and 2 to decrypt: "))
            if choice == 1:
                plaintext = input("Enter yous plain text to encrypt: ")
                print(encrypt(plaintext, key))
            elif choice == 2:
                cipher_text = input("Enter your cipher text to decrypt: ")
                print(decrypt(cipher_text, key))
            else:
                print("We accept only 1 and 2 as input for choose to encrypt or decrypt: ")
                continue
            break
    except (ValueError, OSError):
        print("Key must be in digit ")
        continue
    break
