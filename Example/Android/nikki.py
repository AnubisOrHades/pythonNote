from Example.Android.command import *


def in_game():
    """
    进入游戏
    :return:
    """
    click(400, 1350)
    time.sleep(11)
    click(550, 1695)
    time.sleep(3)
    click(570, 1395)
    time.sleep(3)
    click(500, 1600)
    time.sleep(8)
    print("已进入游戏")


def free():
    """
    点击空格
    :return:
    """
    click(950, 1800)
    time.sleep(1)


def go_break():
    """
    返回
    :return:
    """
    click(80, 90)


def house_of_mystery():
    """
    迷之屋
    :return:
    """
    # 进入
    click(700, 350)
    # 幻之阁

    click(350, 1700)
    free()
    time.sleep(1)
    free()
    click(350, 1050)
    click(1050, 810)
    # slide()
    # 迷之阁
    for i in range(4):
        click(200, 1710)
        time.sleep(2)
        free()
        free()
    # 返回主页
    go_break()


def union():
    """
    塔配师联盟
    :return:
    """
    # 进入
    click(800, 730)
    # 委托
    click(550, 1150)
    # 进行任务
    click(890, 1200)
    click(450, 1400)
    free()
    time.sleep(2)
    free()

    click(90, 310)
    # 图书馆
    click(880, 1500)
    for i in range(3):
        click(300, 660)
        free()
    go_break()
    # 返回主页
    go_break()


def dream():
    """
    织梦人学会
    :return:
    """
    # 进入
    click(700, 1050)
    # 学会委托
    click(300, 940)
    y = 800
    for i in range(3):
        click(540, y)
        click(720, 1100)
        free()
        y += 300
    free()

    # 浮梦岛
    click(300, 1500)
    click(300, 1750)
    free()
    time.sleep(1)
    free()
    # 返回主页
    go_break()
    go_break()


def garden():
    """
    御园琼芳
    :return:
    """
    # 进入
    slide(800, 1100, 200, 1100)
    click(850, 1500)
    # 过关
    click(90, 1660)
    click(600, 970)
    free()
    time.sleep(1)
    free()

    click(970, 1660)
    click(600, 970)
    free()
    time.sleep(1)
    free()

    # 返回主页
    go_break()


def sports():
    """
    搭配竞技场
    :return:
    """
    # 进入
    click(170, 540)
    # 登台
    for i in range(4):
        click(550, 1570)
        click(870, 1600)
        free()
        time.sleep(1.5)
        free()

    # 返回主页
    go_break()


def cabana():
    """
    小屋家具
    :return:
    """
    # 进入
    click(850, 1700)
    # 愿之庭
    click(1000, 1240)
    y = 350 + 400
    for i in range(3):
        click(500, y)
        click(350, 1750)
        free()
        time.sleep(1)
        free()
        click(350, 1070)
        go_break()
        y += 400
    go_break()
    # 返回主页
    go_break()


def open_box(n):
    """
    打开失落之匣
    :return:
    """
    code = "adb shell input tap {} {}".format(100, 230)
    for i in range(n):
        os.system(code)
        time.sleep(0.5)
        click(100, 230)
        free()


def furniture(n):
    """
    获取家具
    :param n: 票数量
    :return:
    """
    click(880, 420)
    n = n // 5
    for i in range(n):
        print(1)
        click(740, 1000)
        time.sleep(1)
        print(2)
        click(970, 1670)
        print(3)
        click(530, 1540)
    free()


def reward():
    """
    领取奖励
    :return:
    """
    click(1000, 500)
    for i in range(12):
        click(900, 850)
        free()

    time.sleep(1)
    x = 250
    for i in range(5):
        click(x, 670)
        free()
        x += 160


def buy():
    """
    购买灵幔
    :return:
    """
    # 进入商店
    click(200, 1400)
    slide(500, 1500, 500, 750)
    # 购买3件灵幔
    click(660, 1300)
    click(800, 850)
    click(850, 840)
    click(850, 840)
    click(750, 1150)
    # 返回主页
    go_break()


def decompose():
    """
    分解灵幔
    :return:
    """

    # 进入分解
    click(250, 1000)
    click(550, 1300)
    # 分解灵幔
    long_press(150, 1300)
    click(550, 800)
    click(720, 1070)
    for i in range(3):
        time.sleep(1)
        free()
    # 返回主页
    go_break()


def end_game():
    """
    退出游戏
    :return:
    """
    break_adb()
    click(550, 1600)


def judges():
    """
    当评委
    :return:
    """
    click(120, 760)
    time.sleep(2)
    click(670, 1800)
    time.sleep(2)
    for i in range(30):
        click(800, 1720)
        time.sleep(3)
    go_break()
    time.sleep(2)
    go_break()


def my_task():
    """
    过关做任务
    :return:
    """
    click(80, 310)
    click(610, 520)
    x = 300
    y = 1300
    for i in range(1, 7):
        click(x, y)
        click(800, 900)
        click(470, 1400)
        click(450, 1400)
        free()
        time.sleep(2)
        free()
        click(80, 300)
        if i % 2 == 1:
            x += 500
        else:
            y += 130
            x -= 500
    free()


def change_clothes(collocation):
    """
    更换搭配
    :param collocation: 搭配列表
    :return:
    """
    click(800, 1400)
    click(60, 880)
    # 清空搭配
    click(680, 1580)
    # 切换adbkeyboard输入法
    os.system("adb shell ime set com.android.adbkeyboard/.AdbIME")
    for clothes in collocation:
        # 搜索
        click(680, 1000)
        # 输入衣服
        click(500, 820)
        input_abd(clothes)
        click(500, 300)
        # 选中衣服
        click(900, 170)
    # 保存搭配
    click(160, 1780)
    # 切换搜狗输入法
    os.system("adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
    go_break()


def task():
    # 开始任务
    click(840, 1400)
    click(980, 1850)
    click(720, 1050)
    # 选择搭配
    click(680, 1220)
    click(930, 520)
    click(170, 1770)

    click(915, 1770)
    time.sleep(1)
    click(170, 1770)
    time.sleep(1)
    click(670, 1770)
    time.sleep(1)
    click(460, 1770)
    time.sleep(1)
    click(170, 1770)

    free()
    free()
    free()
    free()


def run():
    """
    运行奇迹暖暖自动化脚本
    :return:
    """
    while 1:
        mobile = devices()
        if mobile is not None:
            print("手机已连接")
            break
        else:
            print("手机未连接，请连接手机，打开USB调试")
    # 进入游戏
    # in_game()
    # 任务    25
    # my_task()
    print("已过6关")
    # 迷之屋   15
    house_of_mystery()
    print("迷之屋已完成")
    # 搭配师联盟 20
    union()
    print("搭配师联盟任务已完成")
    # 织梦人学会 10
    dream()
    print("织梦人学会任务已完成")
    # 御园琼芳
    garden()
    print("御园琼芳任务已完成")
    # 搭配竞技场 10
    sports()
    print("竞技场任务已完成")
    # 购买物品  10
    buy()
    print("购买物品任务已完成")
    # 分解物品  10
    decompose()
    print("分解物品任务已完成")
    # 当评委   15
    judges()
    print("评委任务已完成")
    # 领取奖励  10
    reward()
    print("今日奖励以领取完毕")
    # 退出游戏
    # end_game()
    print("奇迹暖暖自动化脚本，已运行结束")


if __name__ == '__main__':
    wem = ""
    run()
    # collocation = ["莹缀彩结", "欢愉魔法", "萌宠之心", "彩夜星光", "舞动梦想·华丽", "吉祥花结",
    #                "冠蓝鸦", "彩虹奶霜", "暖心相伴", "绮梦星光", "暖心玩偶·头", "雷克斯暴龙",
    #                "镂空小礼袖", "梦幻之辉", "瑰丽人生", "恢宏时代"]
    # # change_clothes(collocation)
    # task()
