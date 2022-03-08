from random import randrange

value_to_find = 0
mode = 0
found = False


def select_mode():
    global mode
    mode = int(input("Select your game mode : \n"
                     "0 for easy (you try until you find)\n"
                     "1 for hard (you have 10 tries)\n"))


def get_user_value():
    return int(input("Choose a number between 0 and 100\n"))


def play_game():
    select_mode()
    select_random_value()
    if mode == 0:
        while not found:
            check_more_or_less(get_user_value())
    else:
        for _ in range(10):
            check_more_or_less(get_user_value())
            if found:
                break


def select_random_value():
    global value_to_find
    value_to_find = randrange(100)


def check_more_or_less(user_value):
    if user_value < value_to_find:
        print("Number to find is higher")
    elif user_value > value_to_find:
        print("Number to find is lower")
    else:
        print("Congrats you found it")
        global found
        found = True


play_game()
