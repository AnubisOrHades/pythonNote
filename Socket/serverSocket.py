import select
import queue
import json
import datetime
import time

from logset import Logger
from news import Message
from socketBase import Client
from phone import Tel
from device import Device
from settings import *

class Sever:
    inputs = []  # 所有连接中的socket对象集合
    outputs = []  # 所有待处理socket对象集合
    message_queues = {}  # queue：对象的消息队列
    clients = {}  # k:id；  v:socket对象

    def __init__(self, host, port, num=100, stopMark=None):
        """
        socket服务创建
        :param host: 主机IP地址
        :param port: 端口号
        :param num: 监听数量
        :param stopMark: 消息终止符
        """
        self.host = host
        self.port = port
        self.listenNum = num
        self.stopMark = stopMark
        self.server = self.Establish()
        self.logAll = self.logFile("all")
        self.logError = self.logFile("error")

    def logFile(self, t):
        i = datetime.datetime.now()
        i = '%s-%s-%s' % (i.year, i.month, i.day)
        file = Logger('log/%s %s.log' % (i, t), level='debug')
        return file

    def Establish(self):
        """
        初始化服务
        :return:
        """
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(self.listenNum)
        print("正在监听...........")
        # self.logAll.logger.info("服务已开启")
        Sever.inputs.append(server)
        return server

    def receive_client(self, readable):
        """
        处理有动作的socket服务
        :param readable: 动作的socket服务列表
        :return:
        """
        for s in readable:
            # 有新客户端接入
            if s is self.server:
                conn, client_addr = s.accept()
                print("新连接来自于：", client_addr)
                conn.setblocking(0)
                Sever.inputs.append(conn)  # 将连接对象添加到监控队列
                Sever.message_queues[conn] = queue.Queue()  # 创建连接消息队列
                self.logAll.logger.info("%s:%d连接服务器" % (client_addr[0], client_addr[1]))
            # 服务端接收客户端数据
            else:
                news = ""
                data = s.recv(10240)
                data = str(data, 'utf-8')
                # data = str(data, "gbk")
                if data:
                    news += data
                    mowei = data[-4:]
                    if mowei == self.stopMark:
                        news = json.loads(news[0:-4])
                        Sever.message_queues[s].put(news)  # 创建连接消息队列

                        m = Message(news)  # 实例化消息类
                        client = Client(s, m)  # 实例化连接对象
                        client.message = news  # 将消息添加进连接
                        Sever.clients[client.id] = client  # 将连接对象添加到连接池
                        self.logAll.logger.info(
                            "收到来自[%s]的数据:%s" % (s.getpeername()[0], news))
                        # 如果socket对象不在待处理队列，将其添加到待处理队列
                        if s not in Sever.outputs:
                            # 为了不影响处理与其它客户端的连接 , 这里不立刻返回数据给客户端
                            Sever.outputs.append(s)
                    print("收到来自[%s]的数据:" % s.getpeername()[0], data)

                # 如果收不到data代表什么呢? 代表客户端断开了呀
                else:
                    print("客户端断开了", s)
                    # self.logAll.logger.info("客户端断开了", s)
                    if s in Sever.outputs:
                        Sever.outputs.remove(s)  # 清理已断开的连接

                    Sever.inputs.remove(s)  # 清理已断开的连接
                    # if Sever.message_queues[s]["id"] in Sever.clients:
                    #     del Sever.clients[Sever.message_queues[s]["id"]]
                    del Sever.message_queues[s]  # 清理已断开的连接
                    errorS = ""
                    for k, v in Sever.clients.items():
                        if v.socketObj == s:
                            errorS = k
                            break
                    del Sever.clients[errorS]

    def dispose_recive(self, writeable):
        for s in writeable:
            try:
                next_msg = Sever.message_queues[s].get_nowait()
                m = Message(next_msg)

                if m.action == "heartbeat":
                    cl = Client(s, m)
                    cl.heartbeat(Sever.clients)
                else:
                    if m.type == "tel":
                        if m.action == "deviceOperation":
                            cl = Tel(s, m)
                            cl.deviceOperation(Sever.clients)
                    elif m.type == "device":
                        cl = Device(s, m)
                        if m.action == "linkageOperation01":
                            cl.linkageOperation(Sever.clients)
                        else:
                            cl.zhuanfa(Sever.clients)


                    elif m.action == "sendNews":
                        self.sendMessage(s, next_msg)

            except queue.Empty:
                print("client [%s]" % s.getpeername()[0], "queue is empty..")
                # Sever.message_queues[s]["message"] = ""
                Sever.outputs.remove(s)

    def error_client(self, exeptional):
        for s in exeptional:
            print("handling exception for ", s.getpeername())
            Sever.inputs.remove(s)
            if s in Sever.outputs:
                Sever.outputs.remove(s)
            s.close()

            del Sever.message_queues[s]
            errorS = ""
            for k, v in Sever.clients.items():
                if v.socketObj == s:
                    errorS = k
                    break
            del Sever.clients[errorS]
            time.sleep(0.1)

    def sendMessage(self, obj, m):
        """
        客户端A发送给B
        :param obj:
        :param data:
        :return:
        """
        sendId = m.data.get("id")
        if sendId in self.clients:
            try:
                self.clients[sendId].socketObj.send(m.result(id=sendId, d=m.data.get("message")))
            except Exception as e:
                print(e)
                m.responseResult = "NO"
                m.resultCode = 10000
            obj.send(m.result())

    def run(self):
        # server = self.Establish()
        while True:
            try:
                print("waiting for next event".center(100, "-"))
                # 如果没有任何fd就绪,那程序就会一直阻塞在这里
                readable, writeable, exeptional = select.select(Sever.inputs, Sever.outputs, Sever.inputs)

                self.receive_client(readable)
                self.dispose_recive(writeable)
                self.error_client(exeptional)
            except Exception as e:
                self.logError.logger.error(e)
                print(e)


if __name__ == '__main__':
    # hostname = socket.gethostname()
    # # 获取本机IP
    # host = socket.gethostbyname(hostname)
    # host = "172.26.205.127"
    port = 9999
    zhongZhiFu = '/r/n'
    print("主机端口：%s:%d\t\n终止符：%s" % (HOST, PORT, STOPWORD))
    shan = Sever(HOST, PORT, stopMark=STOPWORD)
    shan.run()
