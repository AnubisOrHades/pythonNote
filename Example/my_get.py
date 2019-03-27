import sys
from you_get import common as you_get  # 导入you-get库


def down_load(local_path, url):
    """
    使用you_get下载视频到本地
    :param local_path: 保存地址
    :param url: 视频连接
    :return:
    """
    try:
        print("开始".center(120, "="))
        sys.argv = ['you-get', '-o', local_path, url]  # sys传递参数执行下载，就像在命令行一样
        you_get.main()
        print("下载完成".center(120, "="))
    except Exception as e:
        print(e, "\n", url)


def run(local_path, url):
    t = type(url)
    if t is list:
        for u in url:
            try:
                down_load(local_path, u)
            except Exception as e:
                print("Error:{}\nErrorUrl:{}".format(e, u))
    elif t is str:
        try:
            down_load(local_path, url)
        except Exception as e:
            print("Error:{}\nErrorUrl:{}".format(e, url))
    else:
        print("url参数错误！！！")


if __name__ == '__main__':
    path = r"D:\Anubis\Video"
    urlList = ["https://www.bilibili.com/video/av17732263?p={}".format(i) for i in range(4, 15)]
    url = 'https://www.bilibili.com/video/av46495287?p=2'
    run(path, url)
