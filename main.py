
def encrypt(message, magnitude, shift):
    encrypted_message = ""

    for index in range(len(message)):
        character = ord(message[index])
        encrypted_char = character * magnitude
        encrypted_char = encrypted_char + shift
        encrypted_char = chr((encrypted_char % 26) + 65)  # Mod 26 to stay in the alphabet, + 65 for ASCII Table
        encrypted_message = encrypted_message + encrypted_char

    return encrypted_message


def decrypt(encrypted_message, magnitude, shift):
    decrypted_message = ""

    for index in range(len(encrypted_message)):
        character = ord(encrypted_message[index])
        decrypted_char = character - shift
        decrypted_char = decrypted_char * (find_inverse(magnitude))
        decrypted_char = chr((decrypted_char % 26) + 65)  # Mod 26 to stay in the alphabet, + 65 for ASCII Table
        decrypted_message = decrypted_message + decrypted_char

    return decrypted_message


def find_inverse(num):
    i = 1
    while True:
        check = num * i
        if check % 26 is 1:
            return i
        i = i + 1


def main():
    x = 3
    y = 6
    message = input("Enter the message to encrypt!\n")

    check = input("Do you want to choose a magnitude (a) and shift(b)? (y/n)")
    if check is "y":
        x = int(input("Enter magnitude(a). "))
        y = int(input("Enter shift(b). "))

    encrypted_message = encrypt(message, x, y)
    print("The encrypted message is: " + encrypted_message)

    decrypted_message = decrypt(encrypted_message, x, y)
    print("The decrypted message is: " + decrypted_message)

    return


if __name__ == "__main__":
    main()
