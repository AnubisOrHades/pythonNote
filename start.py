import os
import threading

tasks = [
    {"code": "jupyter notebook", "program": "jupyter notebook"},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
    {"code": "", "program": ""},
]


def execute(num):
    print(tasks[int(num) - 1])
    os.system(tasks[int(num) - 1]["code"])


def run():
    for index, task in enumerate(tasks):
        print("{}\t{}".format(index + 1, task["program"]), end="\t\t")
        if (index + 1) % 3 == 0:
            print()
    print()
    print("按b键退出")
    while 1:
        choice = input("请选择程序的启动编号>>>")
        if choice == "b":
            break
        try:
            # execute(choice)
            t = threading.Thread(target=execute, args=choice)
            t.start()
            t.join()
        except:
            print("序号输入错误")
        else:
            print("{}已经启动成功！")


def test(*args):
    for i in args:
        print(i)


if __name__ == '__main__':
    run()
    # threading.Thread(target=execute, args="1").start()
