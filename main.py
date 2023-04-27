import random, os


def exercise(arg):
    check = None
    try_again = 'y'
    number = random.randint(0,1000)
    while check != True and try_again == 'y':
        os.system("clear")

        if arg == 'b':
            answer = input(f"If you want to exit input \"exit\"\n\nWhat is {number} equivalent in binary?\n-> ")
            check = "0b" + answer == str(bin(number))
        elif arg == 'h':
            answer = input(f"If you want to exit input \"exit\"\n\nWhat is {number} equivalent in hexadecimal?\n-> ")
            check = "0x" + answer == str(hex(number))
        else:
            return

        if check == True:
            check_continue = print("Right answer!")
        else:
            try_again = input("Wrong answer...\nDo you want to try again? [y/n]\n-> ")

if __name__ == "__main__":
    check_continue = None
    while check_continue != "exit" and check_continue != 'n':
        print(
                "If you want to exit input \"exit\"\n",
                "Or press b for binary or h for hexadecimal.",
                sep="\n"
                )
        check_continue = input()
        exercise(check_continue)


