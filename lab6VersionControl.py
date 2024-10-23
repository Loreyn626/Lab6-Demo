
#Loreyn Reid

def pass_to_encode(original):
    res = ""
    for i in original:
        i = int(i)
        i += 3
        if i > 9:
            i -= 10
        res += str(i)

    return res

def decode(encoded_pass):
    decoded_pass = ""
    for digit in encoded_pass:
        if int(digit) <= 2:
            if digit == "2":
                new_digit = 9
            elif digit == "1":
                new_digit = 8
            else:
                new_digit = 7
        else:
            new_digit = (int(digit) - 3)
        decoded_pass += str(new_digit)

    return decoded_pass


def main():


    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            original = input("Please enter your password to encode: ")
            original = pass_to_encode(original)
            print("Your password has been encoded and stored!\n")

        if menu_option == 2:
            decoded_pass = decode(original)
            print(f"The encoded password is {original}, and the original password is {decoded_pass}.\n")

        if menu_option == 3:
            break


if __name__ == "__main__":
    main()




