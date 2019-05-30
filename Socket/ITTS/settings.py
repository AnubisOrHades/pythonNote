import os
import socket

HOST = socket.gethostbyname(socket.gethostname())

PORT = 9999

STOPWORD = '/r/n'

DATABASE = "testdb"

PASSWORD = "111111"

DBHOST = "localhost"


def run():
    path = os.getcwd()  # 获取当前目录
    # 创建log目录
    global PORT
    global STOPWORD
    global DATABASE
    global PASSWORD
    global DBHOST

    with open('{}/settings.txt'.format(path), "r")as f:
        data = f.read()
        for line in data.split("\n"):
            if "PORT" in line:
                PORT = int(line.split()[-1])
            elif "STOPWORD" in line:
                STOPWORD = line.split()[-1]
            elif "DATABASE" in line:
                DATABASE = line.split()[-1]
            elif "PASSWORD" in line:
                PASSWORD = line.split()[-1]
            elif "DBHOST" in line:
                DBHOST = line.split()[-1]
        print("HOST:{}\nPORT:{}\nSTOPWORD:{}\nDATABASE:{}\nPASSWORD:{}\nDBHOST:{}\n".format
              (HOST, PORT, STOPWORD, DATABASE, PASSWORD, DBHOST))
    if not os.path.exists("{}/log".format(path)):
        os.mkdir("{}/log".format(path))
    try:
        from Socket.database.myDB import MysqlClients
        tags = MysqlClients(db=DATABASE, h=DBHOST, p=PASSWORD)
        r = tags.select("product_shanLaiEdition", "editionName", "1.0.0", key2="id")
    except Exception as e:
        if e.args[0] == 1045:
            print("请检查数据库配置")


if __name__ == '__main__':
    run()

