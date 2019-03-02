import os
import time


class File:
    """
    path:文件地址
    name:文件名
    extension_name:文件扩展名
    size:文件大小
    creation_time:文件创建时间
    modification_time:文件修改时间
    access_time:文件访问时间
    """
    def __init__(self, path):
        self.path = path
        self.name = self.gie_name()[0]
        self.extension_name = self.gie_name()[-1]
        self.size = self.get_size()
        self.creation_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(self.path)))
        self.modification_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(self.path)))
        self.access_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getatime(self.path)))

    @staticmethod
    def format_size(byte):
        try:
            byte = float(byte)
            kb = byte / 1024
        except Exception as e:
            print("传入的字节格式不对\n", e)
            return "Error"

        if kb >= 1024:
            m = kb / 1024
            if m >= 1024:
                g = m / 1024
                return "%.2fG" % g
            else:
                return "%.2fM" % m
        else:
            return "%.2fkb" % kb

    @staticmethod
    def kb(byte):
        try:
            byte = float(byte)
            kb = byte / 1024
        except Exception as e:
            print("传入的字节格式不对\n", e)
            return "Error"
        return kb

    @staticmethod
    def mb(byte):
        try:
            byte = float(byte)
            mb = byte / 1024 / 1024
        except Exception as e:
            print("传入的字节格式不对\n", e)
            return "Error"
        return mb

    @staticmethod
    def gb(byte):
        try:
            byte = float(byte)
            gb = byte / 1024 / 1024 / 1024
        except Exception as e:
            print("传入的字节格式不对\n", e)
            return "Error"
        return gb

    def get_size(self):
        """
        获取文件大小
        :return: 件大小
        """
        size = os.path.getsize(self.path)
        return self.format_size(size)

    def gie_name(self):
        """
        获取文件名
        :return: 文件名
        """
        lis = self.path.split("\\")
        name = lis[-1].split(".")
        return name

    def attribute(self):
        """
        文件属性
        :return:
        """
        attribute = "位置：{}\n文件名：{}\n扩展名：{}\n大小：{}\n" \
                    "创建时间：{}\n修改时间：{}\n访问时间：{}\n" \
            .format(self.path, self.name, self.extension_name, self.size,
                    self.creation_time, self.modification_time, self.access_time)
        print(attribute)
        return attribute

    def rename(self, name):
        """
        重命名
        :param name: 新文件名
        :return:
        """
        lis = self.path.split("\\")
        lis[-1] = "{}.{}".format(name, self.extension_name)
        new_name = "\\".join(lis)
        os.rename(self.path, new_name)
        print(new_name)

    def __str__(self):
        attribute = "位置：{}\n文件名：{}\n扩展名：{}\n大小：{}\n" \
                    "创建时间：{}\n修改时间：{}\n访问时间：{}\n" \
            .format(self.path, self.name, self.extension_name, self.size,
                    self.creation_time, self.modification_time, self.access_time)
        return attribute


if __name__ == '__main__':
    s = File(r'D:\360安全浏览器下载\taotubj.png')
    s.attribute()
