import os
import socket

HOST = socket.gethostbyname(socket.gethostname())

PORT = 9999

STOPWORD = '/r/n'

DATABASE = "testdb"

PASSWORD = "111111"


def run():
    path = os.getcwd()  # 获取当前目录
    # 创建log目录
    with open('{}/settings.txt'.format(path), "r")as f:
        data = f.read()
        for line in data.split("\n"):
            if "PORT" in line:
                PORT = line.split()[-1]
            elif "STOPWORD" in line:
                STOPWORD = line.split()[-1]
            elif "DATABASE" in line:
                DATABASE = line.split()[-1]
            elif "PASSWORD" in line:
                PASSWORD = line.split()[-1]
        print("HOST:{}\nPORT:{}\nSTOPWORD:{}\nDATABASE:{}\nPASSWORD:{}\n".format(HOST, PORT, STOPWORD, DATABASE,
                                                                                 PASSWORD))
    if not os.path.exists("{}/log".format(path)):
        os.mkdir("{}/log".format(path))


run()

if __name__ == '__main__':
    run()
