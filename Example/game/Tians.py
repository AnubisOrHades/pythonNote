from Example.winInput import *


def run(data):
    key_input("caps_lock")
    for code in data:
        print(code)
        key_input("enter")
        for i, word in enumerate(code.split(" ")):
            for letter in word:
                key_input(letter)
            if word != code.split(" ")[-1]:
                key_input("spacebar")
        mouse_click((540, 140))
    key_input("caps_lock")


if __name__ == '__main__':
    "mount olympus"
    time.sleep(4)
    code_list = ["trojan horse for sale", "atm of erebus", "junk food night"]
    # key_input("caps_lock")
    for i in range(30):
        run(code_list)
        # code = "atm of erebus"
    #         # key_input("enter")
    #         # for i, word in enumerate(code.split(" ")):
    #         #     for letter in word:
    #         #         key_input(letter)
    #         #     if word != code.split(" ")[-1]:
    #         #         key_input("spacebar")
    #         # mouse_click((540, 140))
    """
    
    """
    # key_input("spacebar")
