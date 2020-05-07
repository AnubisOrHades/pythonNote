import threading
import queue
from tools.down_load.my_get import down_load

tasks = queue.Queue()


class Threading:
    """
    多线程
    :param queue: 任务队列
    :param fun:执行函数
    :param thread_count:创建线程数量

    """

    def __init__(self, queue, fun, thread_count):
        self.queue = queue
        self.fun = fun
        self.cont = thread_count

    def start(self):
        while not self.queue.empty():
            thList = []
            for i in range(self.cont):
                task = self.queue.get()
                t = threading.Thread(target=self.fun, args=task)
                thList.append(t)
                t.start()
                print("第{}线程开始".format(i).center(80, "="))
            for th in thList:
                th.join()


if __name__ == '__main__':
    urls = ["https://www.bilibili.com/video/av27076260/?p=%d" % i for i in range(1, 20)]
    for u in urls:
        down_load("C:\pySpark", u)
        # tasks.put(("C:\pySpark", u))

    # c = Threading(tasks, down_load, 5)
    # c.start()
