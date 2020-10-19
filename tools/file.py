import os
import hashlib


class File(object):
    def __init__(self, p, n):
        """
        初始化文件
        :param p: 文件路径，所在文件夹
        :param n: 文件名
        """
        self.path = p
        self.name = n
        self.size = self.get_size()
        # self.md5 = self.get_md5()
        pass

    def get_size(self):
        """
        获取文件大小
        :return:
        """
        f_size = os.path.getsize("{}\\{}".format(self.path, self.name))
        f_size = round(f_size, 2)
        if f_size < 1024:
            print("{}B".format(round(f_size, 2)))
        elif f_size < 1024 * 1024:
            print("{}KB".format(round(f_size / 1024, 2)))
        elif f_size < 1024 * 1024 * 1024:
            print("{}MB".format(round(f_size / 1024 / 1024, 2)))
        elif f_size < 1024 * 1024 * 1024 * 1024:
            print("{}GB".format(round(f_size / 1024 / 1024 / 1024, 2)))

        return round(f_size, 2)

    def get_md5(self):
        """
        获取文件md5
        :return:
        """
        md5_obj = hashlib.md5()
        with open("{}\\{}".format(self.path, self.name), "rb")as f:
            md5_obj.update(f.read())
            result = md5_obj.hexdigest()
        return result

    def __str__(self):
        return ""


if __name__ == '__main__':
    path = r"D:\Anubis\VM\ubuntu-18"
    name = "Ubuntu 64 位-s001.vmdk"
    F = File(path, name)
    print(F.size)
