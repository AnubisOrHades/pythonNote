import os
import time
import hashlib


def devices():
    ip_port = os.popen("adb devices")
    data = ip_port.read()
    lis = data.split("\n")
    device_code = lis[1][:9]
    print(device_code)
    ip_port.close()
    return device_code


def home():
    """
    home键
    :return:
    """
    os.system("adb shell input keyevent 3")


def break_adb():
    """
    返回键
    :return:
    """
    os.system("adb shell input keyevent 4")


def menu():
    os.system("adb shell input keyevent 82")


def click(x, y, t=1.0):
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


def long_press(x, y, t=1):
    """
    长按
    :param x: x坐标
    :param y: y坐标
    :param t: 休眠时间
    :return:
    """
    code = "adb shell input swipe {} {} {} {} 1200".format(x, y, x, y)
    os.system(code)
    time.sleep(t)


def slide(x, y, x1, y1, s, t=1):
    """
    滑动
    :param x:开始x坐标
    :param y:开始y坐标
    :param x1:结束x坐标
    :param y1:结束y坐标
    :param s:滑动时间 毫秒
    :param t: 休眠时间
    :return:
    """
    code = "adb shell input swipe {} {} {} {} {}".format(x, y, x1, y1, s)
    os.system(code)
    time.sleep(t)


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
    os.system("adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
    time.sleep(1)


def screenshot(pc_path=""):
    """
    手机截图上传PC
    :param pc_path: 图片在PC上的路径
    :return: None
    """
    try:
        # 生成文件路径，文件名为MD5加密时间戳
        file_path = r"/sdcard/截屏/{}.png".format(
            hashlib.md5(str(time.time()).encode()).hexdigest()[8:-8])

        # 截屏
        os.system("adb shell screencap -p {file_path}".format(file_path=file_path))
        # 上传至指定文件夹
        os.system("adb pull {} {}".format(file_path, pc_path))
        # 删除手机截屏
        os.system("adb shell rm {}".format(file_path))
    except Exception as e:
        print("Error:{}".format(e))
    else:
        pass
    finally:
        pass


def quiet():
    """
    调节手机媒体音量至静音
    :return:
    """
    try:
        for i in range(15):
            os.system("adb shell input keyevent 25")
        pass
    except Exception as e:
        print("Error:{}".format(e))
    else:
        pass
    finally:
        pass


if __name__ == '__main__':
    """"""
    # 查看输入法列表
    # os.system("adb shell ime list")
    # 切换adbkeyboard输入法
    # os.system("adb shell ime set com.android.adbkeyboard/.AdbIME")
    # 切换搜狗输入法
    # os.system("adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
    # os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '上海-悠悠'")
    # devices()
    # slide(500,200,500,1000,0.5)
    # click(500,500)
    # os.system("adb shell input swipe 500 200 500 1000")
    for i in range(34):
        click(500, 2000)
