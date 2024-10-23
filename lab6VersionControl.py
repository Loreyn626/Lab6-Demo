
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
            print("Your password has been encoded and stored!")


        if menu_option == 3:
            break


if __name__ == "__main__":
    main()




