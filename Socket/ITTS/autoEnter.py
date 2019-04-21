import time
import win32api
import win32con
from ctypes import *


class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


def get_mouse_point():
    """
    获取鼠标位置
    :return: 返回鼠标位置坐标
    """
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    print(int(po.x), int(po.y))
    return int(po.x), int(po.y)


def mouse_move(coordinates):
    """
    移动鼠标到coordinates位置
    :param coordinates: 坐标（x,y）
    :return:
    """
    windll.user32.SetCursorPos(coordinates[0], coordinates[1])
    time.sleep(0.05)


def mouse_click(coordinates=None):
    """
    鼠标单击
    :param coordinates: 单击位置，如果不为空则，先移动鼠标到指定坐标，然后单击
    :return:
    """
    if coordinates is not None:
        mouse_move(coordinates)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(0.05)


if __name__ == '__main__':
    while 1:
        mouse_click((800, 400))
        time.sleep(10)
