import os


# 递归遍历目录
def getAlldirInDiGui(path):
    filesList = os.listdir(path)
    print(filesList)
    for fileName in filesList:
        fileAbpath = os.path.join(path, fileName)
        if os.path.isdir(fileAbpath):
            print("目录：", fileName)
            getAlldirInDiGui(fileAbpath)
        else:
            print("普通文件", fileName)


# 传递参数的时候，注意需要写上（r）表明传递的是路径
getAlldirInDiGui(r"D:\迅雷下载")


