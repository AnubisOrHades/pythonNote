"""
死灵法师辅助脚本：
按“A”时启用脚本
按“B”退出脚本
开局进入图书馆
游戏是定时按2键使用骨甲
"""

import threading
import pyHook
import pythoncom

from Example.win.winInput import *


def goto_library():
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
    mouse_click((700, 220))
    print("角色已进入 佐敦-库的图书馆！")


def siling():
    goto_library()
    time.sleep(0.5)
    while 1:
        time.sleep(5)
        key_input("2")
        pass


def onKeyboardEvent(event):
    windowTitle = create_string_buffer(512)
    windll.user32.GetWindowTextA(event.Window, byref(windowTitle), 512)

    if event.Key == "A":
        print("脚本启动")
        k = threading.Thread(target=siling)
        k.start()


    elif event.Key == "B":
        print("脚本结束")

    return True


def key_listen():
    # 安装钩子，监听键盘消息

    hm = pyHook.HookManager()

    hm.KeyDown = onKeyboardEvent

    hm.HookKeyboard()

    pythoncom.PumpMessages()


def run():
    key_listen()


if __name__ == '__main__':
    time.sleep(5)
    siling()
