from Example.Android.command import *


def switch_app():
    """
    切换到上一个应用
    :return:
    """
    os.system("adb shell input keyevent 187")
    click(430, 1200)


def creat_note(n):
    """
    创建新便签
    :param n: 内容
    :return:
    """
    # 切换到便签
    switch_app()
    # 创建新便签
    click(1000, 100)
    click(500, 500)
    input_abd(n)
    click(980, 1820)  # 换行
    click(1000, 130)
    # 切换到浏览器
    switch_app()
    pass


def copy_to_note(y, x=550):
    """
    复制浏览器收藏书签
    :param y: y坐标
    :param x: x坐标
    :return:
    """
    # 长按书签
    long_press(x, y)
    # 选择编辑书签
    click(x - 75, y + 350)
    # 复制收藏名
    click(40, 380, 0.2)  # 移动光标
    long_press(40, 380)  # 收藏菜单
    click(220, 250)  # 全选
    click(220, 250)  # 复制
    # 切换到便签
    switch_app()
    # 粘贴到便签
    click(550, 300)  # 进入便签
    click(500, 500)  # 光标
    click(640, 1160)  # 选项
    click(900, 1450)  # 粘贴
    click(980, 1820)  # 换行
    click(1000, 130)  # 完成
    # 切换到浏览器
    switch_app()

    # 复制收藏链接
    click(40, 537, 0.2)  # 移动光标
    long_press(40, 537)  # 收藏菜单
    click(220, 370)  # 全选
    click(220, 370)  # 复制
    # 切换到便签
    switch_app()
    # 粘贴到便签
    click(550, 300)  # 进入便签
    click(500, 500)  # 光标
    click(640, 1160)  # 选项
    click(900, 1450)  # 粘贴
    click(980, 1820)  # 换行
    click(1000, 130)  # 完成
    # 切换到浏览器
    switch_app()
    # 返回书签页面
    click(70, 150)
    pass


def run():
    # 打开浏览器
    os.system("adb shell input keyevent 64")
    time.sleep(2)
    # 打开便签

    # 切换到浏览器
    # 菜单
    menu()
    time.sleep(1)
    # 书签
    click(360, 1350)
    # 便签数量
    collection_num = 0
    y = 300
    while 1:
        if collection_num % 9 == 1:
            # 创建便签
            creat_note(collection_num // 9 + 1)
            pass
        # 复制书签
        copy_to_note(y)
        collection_num += 1
        if collection_num % 9 == 0:
            # 向上滑动
            slide(550, 1730, 550, 300, 1500)
            # 新建便签

            y = 300
            pass
        else:
            y += 175
        print(y)

    pass


if __name__ == '__main__':
    # run()
    copy_to_note(300)
    pass
