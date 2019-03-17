import sys
from you_get import common as you_get  # 导入you-get库


def down_load(path, url):
    """
    使用you_get下载视频到本地
    :param path: 保存地址
    :param url: 视频连接
    :return:
    """
    print("开始".center(120, "="))
    sys.argv = ['you-get', '-o', path, url]  # sys传递参数执行下载，就像在命令行一样
    you_get.main()
    print("下载完成".center(120, "="))


if __name__ == '__main__':
    down_load("D:\\", "http://www.365yg.com/i6650101575308034563/#mid=1618088888118279")
