import os
import time


def devices():
    ip_port = os.popen("adb devices")
    data = ip_port.read()
    lis = data.split("\n")
    device_code = lis[1][:9]
    print(device_code)
    ip_port.close()
    return device_code


def home():
    os.system("adb shell input keyevent 3")


def break_adb():
    os.system("adb shell input keyevent 4")


def click(x, y, t=2):
    """
    单击
    :param x: x坐标
    :param y: y坐标
    :param t: 休眠时间
    :return:
    """
    code = "adb shell input tap {} {}".format(x, y)
    os.system(code)
    time.sleep(t)


def long_press(x, y, t=2):
    """
    长按
    :param x: x坐标
    :param y: y坐标
    :param t: 休眠时间
    :return:
    """
    code = "adb shell input swipe {} {} {} {} 1200".format(x, y, x, y)
    os.system(code)
    time.sleep(2)


def slide(x, y, x1, y1, t=2):
    """
    滑动
    :param x:开始x坐标
    :param y:开始y坐标
    :param x1:结束x坐标
    :param y1:结束y坐标
    :param t: 休眠时间
    :return:
    """
    code = "adb shell input swipe {} {} {} {} 300".format(x, y, x1, y1)
    os.system(code)
    time.sleep(2)


def input_abd(text):
    """
    文本输入
    :param text:要输入的文本
    :return:
    """
    # 切换adbkeyboard输入法
    os.system("adb shell ime set com.android.adbkeyboard/.AdbIME")

    code = "adb shell am broadcast -a ADB_INPUT_TEXT --es msg {}".format(text)
    os.system(code)
    # 切换搜狗输入法
    # os.system("adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
    time.sleep(2)


if __name__ == '__main__':
    """"""
    # 查看输入法列表
    # os.system("adb shell ime list")
    # 切换adbkeyboard输入法
    # os.system("adb shell ime set com.android.adbkeyboard/.AdbIME")
    # 切换搜狗输入法
    # os.system("adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
    # os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '上海-悠悠'")
    devices()
