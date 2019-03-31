"""
暗黑3自动脚本
1.开局进入第二营地
2.开启小秘境
"""
from Example.winInput import *


def goto_caldeum():
    """
    进入卡尔蒂姆
    :return:
    """
    key_input("m")
    mouse_click((715, 99))
    mouse_click((817, 415))
    mouse_click((830, 630))
    print("角色已进入卡尔蒂姆秘密营地！")


def open_secret():
    """
    在卡尔蒂姆开启小秘境
    :return:
    """
    mouse_click((100, 400))
    time.sleep(5)
    mouse_click((212, 224))
    mouse_click((218, 670))
    mouse_click((610, 318))
    print("小秘境已开启！")


if __name__ == '__main__':
    time.sleep(5)
    open_secret()
