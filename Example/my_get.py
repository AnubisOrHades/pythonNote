import sys
from you_get import common as you_get  # 导入you-get库


def down_load(local_path, url, name=None):
    """
    使用you_get下载视频到本地
    :param local_path: 保存地址
    :param name:文件名
    :param url: 视频连接
    :return:
    """
    try:
        print("开始".center(120, "="))
        sys.argv = ['you-get', '-o', local_path, "-O", name, url]  # sys传递参数执行下载，就像在命令行一样
        you_get.main()
        print("下载完成".center(120, "="))
    except Exception as e:
        print(e, "\n", url)


def down_b_video(path=None, url=None, start=1, end=9):
    """
    下载B站视频
    :param path: 本地保存地址
    :param url: 下载链接
    :param start: 开始位置
    :param end: 结束位置
    :return:
    """
    task_lis = ["{}{}".format(url[:-1], i) for i in range(start, end)]
    print(task_lis)
    for task in task_lis:
        down_load(path, task)


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
    path = r"D:\Anubis\Video\数据分析"
    url = "https://www.bilibili.com/video/av22571713/?p=1"
    # run(path, urlList)
    down_b_video(path, url, start=33,end=92)
