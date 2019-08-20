from Example.Android.command import *


def run():
    # 打开支付宝
    click(700, 1050)
    # 进入我的
    click(1000, 1800)
    # 进入支付宝会员
    click(500, 500)
    time.sleep(2)
    # 领取积分
    click(150, 950)
    time.sleep(2)
    for i in range(5):
        click(500, 700)
    # 返回我的
    break_adb()
    time.sleep(1)
    break_adb()
    # 进入余额宝
    click(500, 1050)
    time.sleep(2)
    # 转入
    click(800, 1050)
    time.sleep(2)
    # 输入金额
    click(500, 800)
    click(150, 1400)
    time.sleep(2)
    click(500, 1150)
    # 返回桌面
    break_adb()
    time.sleep(1)
    break_adb()


if __name__ == '__main__':
    run()
