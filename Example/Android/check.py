from Example.Android.nikki import *


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
    # house_of_mystery()
    print("迷之屋已完成")
    # 搭配师联盟 20
    union()
    print("搭配师联盟任务已完成")
    # 织梦人学会 10
    # dream()
    print("织梦人学会任务已完成")
    # 御园琼芳
    # garden()
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
    # reward()
    print("今日奖励以领取完毕")
    # 退出游戏
    # end_game()
    print("奇迹暖暖自动化脚本，已运行结束")


if __name__ == '__main__':
    # judges()
    run()
    # garden()
    # click(970, 1750)
