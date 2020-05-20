import os
import time


def check_end(file_name):
    """
    检测文件是否下载完成
    :param file_name: 文件名
    :return:
    """
    return os.path.exists(os.path.join(save_path, file_name))


def check_start(file_name):
    """
    检测文件是否开始下载
    :param file_name: 文件名
    :return:
    """
    cache_file = file_name + ".xltd"
    return os.path.exists(os.path.join(save_path, cache_file))


def get_file_name(url):
    """
    获取文件名
    :param url: 下载链接
    :return: 文件名
    """
    return os.path.split(url)[1]


def download(url, re_name=None):
    """
    下载文件
    :param url:
    :param re_name:新文件名
    :return:返回True表示下载完成 否则失败
    """
    os.system(r'"{thunder_path}" {url}'.format(thunder_path=thunder_path, url=url))
    time.sleep(2)
    file_name = get_file_name(url)
    print("正在下载 {}".format(file_name).center(100, "="))
    if check_start(file_name):
        while True:
            # 每分钟检测一次是否下载完成
            time.sleep(6)
            if check_end(file_name):
                if re_name is not None:
                    old_path = os.path.join(save_path, file_name)
                    new_path = os.path.join(save_path, re_name)
                    os.rename(old_path, new_path)
                print("下载完成！！！{}".format(file_name).center(100, "="))
                return True
    else:
        return False


# 迅雷安装位置
thunder_path = r"D:\Program Files\Thunder Network\Thunder\Program\Thunder.exe"
# 文件存储位置，可在迅雷中设置
save_path = r"F:\迅雷下载\Auto"

if __name__ == '__main__':
    # 迅雷安装位置
    thunder_path = r"D:\Program Files\Thunder Network\Thunder\Program\Thunder.exe"
    # 文件存储位置，可在迅雷中设置
    save_path = r"F:\迅雷下载\Auto"

    d_url = "https://d2.xia12345.com/down/89/2020/04/mV1qyEda.mp4"
    file_new_name = "小伙子很粗鲁强行扒女友内裤强上还玩轻sm.mp4"

    download(d_url, file_new_name)
    # print(os.path.exists(os.path.join(save_path, get_file_name(d_url))))
