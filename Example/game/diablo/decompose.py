import os

from Example.win.winInput import *

LEFT_TOP = ""
RIGHT_BOTTOM = ""


def decompose(start_xy, box_x, box_y):
    """
     Diablo物品分解
    :param start_xy: 开始坐标（x，y）
    :param box_x: 盒子宽
    :param box_y: 盒子高
    :return:
    """

    for x in range(9):
        for y in range(6):
            mouse_click(start_xy)
            time.sleep(0.1)
            key_input("enter")
            time.sleep(0.2)
            key_input("enter")
            start_xy[1] += box_y
        start_xy[1] -= box_y * 6
        start_xy[0] += box_x


def run():
    global LEFT_TOP
    global RIGHT_BOTTOM
    path = os.getcwd()
    with open('{}/settings.txt'.format(path), "r")as f:
        data = f.read()
        for line in data.split("\n"):
            if len(line) == 0:
                continue
            txt = line.split("=")[-1].split(",")
            if "LEFT_TOP" in line:
                LEFT_TOP = [int(txt[0].split()[0][1:]), int(txt[1].split()[0][:-1])]
            elif "RIGHT_BOTTOM" in line:
                RIGHT_BOTTOM = [int(txt[0].split()[0][1:]), int(txt[1].split()[0][:-1])]
    print("LEFT_TOP:{}\nRIGHT_BOTTOM:{}".format(LEFT_TOP, RIGHT_BOTTOM))
    box_x = int((RIGHT_BOTTOM[0] - LEFT_TOP[0]) / 9)
    box_y = int((RIGHT_BOTTOM[1] - LEFT_TOP[1]) / 6)
    start_xy = [int(LEFT_TOP[0] + box_x / 2), int(LEFT_TOP[1] + box_y / 2)]
    print("({},{})\n{}".format(box_x, box_y, start_xy))
    print("start".center(100, "="))
    time.sleep(3)
    decompose(start_xy, box_x, box_y)


if __name__ == '__main__':
    run()
