import socket
import select


class SocketClient:
    inputs = []  # 所有连接中的socket对象集合
    outputs = []  # 所有待处理socket对象集合
    message_queues = {}  # queue：对象的消息队列

    def __init__(self, h="23.92.110.230", p=9999, z="/r/n"):
        self.host = h
        self.port = p
        self.obj = self.client()
        self.zhongZhiFu = z
        SocketClient.inputs.append(self.obj)

    def client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        return s

    def send(self, message):
        m = (message + self.zhongZhiFu).encode('utf8')
        print(m)
        self.obj.send(m)

    def receive(self):
        msg = self.obj.recv(1024)
        return msg.decode('utf-8')

    def close(self):
        self.obj.close()

    def run(self):
        # server = self.Establish()
        while True:
            try:
                print("waiting for next event".center(100, "-"))
                # 如果没有任何fd就绪,那程序就会一直阻塞在这里
                readable, writeable, exeptional = select.select(SocketClient.inputs, SocketClient.outputs,
                                                                SocketClient.inputs)
                for s in readable:
                    if s == self.obj:
                        data = self.receive()
                        SocketClient.outputs.append(s)

                for s in writeable:
                    s.send()
            except Exception as e:
                print(e)


if __name__ == '__main__':
    hostname = socket.gethostname()
    # 获取本机IP
    host = socket.gethostbyname(hostname)
    # host = "172.26.205.127"
    port = 9999
    zhongZhiFu = '/r/n'
    c = SocketClient(host, port)
    # c = SocketClient()
    c.send('{"id":"123456","uniqueId":"1bd06403-31b9-476f-ad03-722820",'
           '"action":"heartbeat","messageId":"123456","data":{}}')
    c.close()
