import os


def get_file_size(path):
    """
    获取文件大小
    :param path: 文件路径
    :return: 文件大小
    """
    f_size = os.path.getsize(path)
    return round(f_size, 2)
