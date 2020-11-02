import os
import hashlib

"""
os.walk(path)       获取路径下所有文件夹及文件（包括子文件夹下的文件夹及文件）
os.listdir(path)    获取路径下所有文件夹及文件
os.path.split(path) 分割文件路径及文件名,返回一个元组
os.path.splitext(path)	分割路径中的文件名与拓展名
os.path.exists(path)判断路径是否存在
"""


class File(object):
    def __init__(self, p, n=None):
        """
        初始化文件
        :param p: 文件路径，所在文件夹
        :param n: 文件名
        """
        if "." in p:
            self.path = os.path.split(p)[0]
            self.name = os.path.split(p)[1]
            self.local_path = p
        else:
            self.path = p
            self.name = n
            self.local_path = "{}\\{}".format(self.path, self.name)
        if not os.path.exists(self.local_path):
            print("Error：文件不存在")
            return
        self.size = self.get_size()
        # self.md5 = self.get_md5()
        pass

    def get_size(self):
        """
        获取文件大小
        :return:
        """
        f_size = os.path.getsize(self.local_path)
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
        with open(self.local_path, "rb")as f:
            md5_obj.update(f.read())
            result = md5_obj.hexdigest()
        return result

    def re_name(self, new_name):
        """
        重命名
        :param new_name:
        :return:
        """
        if "." not in new_name:
            new_name = "{}{}".format(new_name, os.path.splitext(self.local_path)[1])
        os.rename(self.local_path, os.path.join(self.path, new_name))

    def __str__(self):
        return ""


def get_file_list(path):
    """
    获取路径下所有文件（包括子文件夹下文件）
    :param path: 路径
    :return: 文件列表
    """
    try:
        file_list = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_list.append(os.path.join(root, file))
        pass
    except Exception as e:
        print("Error:{}".format(e))
    else:
        return file_list
        pass
    finally:
        pass


def repeat_file(path):
    """
    获取文件夹下重复文件
    :param path: 路径
    :return:
    """
    try:
        # 文件-哈希值
        file_md5_dict = {}
        # 哈希值列表
        md5_list = []
        # 重复哈希值
        repeat_md5 = set()
        # 重复文件
        repeat_files = {}
        # 文件列表
        flies = get_file_list(path)

        for flie in flies:
            file_md5_dict[flie] = File(os.path.split(flie)[0], os.path.split(flie)[1]).get_md5()

        for key, value in file_md5_dict.items():
            md5_list.append(value)

        # 获取重复文件的哈希值
        for key, value in file_md5_dict.items():
            if md5_list.count(value) > 1:
                repeat_md5.add(value)

        # 获取重复文件
        for md5 in repeat_md5:
            repeat_files[md5] = []
            for k in file_md5_dict:
                if md5 == file_md5_dict[k]:
                    repeat_files[md5].append(k)

    except Exception as e:
        print("Error:{}".format(e))
    else:
        print(repeat_files)
        return repeat_files
        pass
    finally:
        pass


if __name__ == '__main__':
    pass
    # path = r"D:\Anubis\Video"
    # name = "Ubuntu 64 位-s001.vmdk"
    # F = File(path, name)
    # print(F.size)
    # print(os.listdir(path))
