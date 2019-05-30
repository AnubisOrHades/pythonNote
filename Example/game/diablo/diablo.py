"""
暗黑3自动脚本
1.开局进入第二营地
2.开启小秘境
"""
from Example.winInput import *

MIX_X = 1535
MIX_Y = 863


def goto_caldeum():
    """
    进入卡尔蒂姆
    :return:
    """
    # 打开大地图
    key_input("m")
    # 切换世界地图
    mouse_click((715, 99))
    # 选择卡尔蒂姆地图
    mouse_click((817, 415))
    # 选择秘密营地
    mouse_click((830, 630))
    print("角色已进入卡尔蒂姆秘密营地！")


def open_secret():
    """
    在卡尔蒂姆开启小秘境
    :return:
    """
    # 选择奈非天尖方碑
    mouse_click((100, 400))
    time.sleep(3)
    # 选择小秘境
    mouse_click((212, 230))
    # 打开小秘境
    mouse_click((218, 670))
    time.sleep(3)
    # 进入小秘境
    mouse_click((MIX_X//2-150, MIX_Y//2))
    # time.sleep(1)
    # mouse_click()
    print("小秘境已开启！")


if __name__ == '__main__':
    time.sleep(3)
    goto_caldeum()
    time.sleep(3)
    open_secret()
    # mouse_click((MIX_X//2, MIX_Y//2))
