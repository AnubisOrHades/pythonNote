import os


def run():
    path = os.getcwd()  # 获取当前目录
    # 创建log目录
    if not os.path.exists("{}/log".format(path)):
        os.mkdir("{}/log".format(path))
    os.chdir(path)  # 切换到当前目录
    os.system("python serverSocket.py")  # 命令行启动当前项目


if __name__ == '__main__':
    run()
