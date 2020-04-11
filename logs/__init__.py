import logging
import os
import time
import sys
from logging import Logger

# 设置日志格式（绝对路径）
local_path = r"D:\Anubis\programming\Mypython\pythonNote\logs"


def get_log_path():
    """
    获取日志路径
    :return:
    """
    # local_path = os.path.abspath("logs")
    dir_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    log_path = "{}\\{}".format(local_path, dir_time)
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    return log_path


class NewLog(Logger):
    def __init__(self, name=None):
        super().__init__(name)
        try:
            self.setLevel(logging.DEBUG)

            log_name = "{}//{}.log".format(get_log_path(), os.path.basename(sys.argv[0])[:-3])
            if os.path.exists(log_name):
                mes = ""
            else:
                mes = "path:{}".format(sys.argv[0])

            fh = logging.FileHandler(log_name)
            fh.setLevel(logging.INFO)

            # 再创建一个handler，用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义handler的输出格式
            formatter = logging.Formatter('[%(asctime)s] - %(levelname)s -%(module)s '
                                          '-%(funcName)s -%(lineno)d - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 给logger添加handler
            self.addHandler(fh)
            self.addHandler(ch)
            if len(mes) > 0:
                self.info(mes)
        except Exception as e:
            print("输出日志失败！ %s" % e)


log = NewLog()

if __name__ == '__main__':
    """"""
