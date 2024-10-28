from constants import (
    pattern_all,
    pattern_change,
    pattern_hello,
    pattern_quit,
    pattern_show,
    pattern_add,
    INCORRECT_MESSAGE,
    USAGE,
)
from contact_handler import add_contact, change_contact, show_all, show_contact


"""
    This programm is entry point to phone-book bot. Read README.txt to get more
"""




def main():
    print("Hello, I`m phone-book bot")
    while True:
        user_input = input("Enter your command:  ")
        command, *args = input_parser(user_input)
        if command in pattern_quit:
            print("Have a nice day!")
            break
        if command in pattern_hello:
            print("Glad to see you! \nHow can I help you?")
        elif command in pattern_add:
            add_contact(*args)
        elif command in pattern_change:
            change_contact(*args)
        elif command in pattern_all:
            show_all(*args)
        elif command in pattern_show:
            show_contact(*args)
        else:
            print(INCORRECT_MESSAGE)
            print(USAGE)


def input_parser(user_input: str) -> list():
    if user_input is None or len(user_input.strip()) == 0:
        return "invalid input"
    cmd, *args = user_input.strip().split()
    cmd = cmd.strip().lower()
    return cmd, *args


if __name__ == "__main__":
    main()