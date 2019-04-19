import select
import socket
import sys
import queue

from mySocket.shanLaiSocket.socketClient import *

zhongZhiFu=r"/r/t"
def over(data):
    return data[-4:0] == r"\r\t"


def heartbeat(data):
    # data={"id":"123456","uniqueId":"1bd06403-31b9-476f-ad03-722820","action":"heartbeat","messageId":"123456","data":{}}

    del data["data"]
    data["action"] += "Response"
    data["responseResult"] = "OK"
    data["return"] = []
    return data


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server_addr = ('192.168.171.1', 9999)

# server_addr = ('192.168.171.1',9999)

print('starting up on %s port %s' % server_addr)
server.bind(server_addr)

server.listen(1000)

inputs = [server, ]  # 自己也要监测呀,因为server本身也是个fd

clients = {}

outputs = []

message_queues = {}

while True:
    print("waiting for next event...")
    # 如果没有任何fd就绪,那程序就会一直阻塞在这里
    readable, writeable, exeptional = select.select(inputs, outputs, inputs)

    for s in readable:  # 每个s就是一个socket
        if s is server:
            """
            别忘记,上面我们server自己也当做一个fd放在了inputs列表里,传给了select,
            如果这个s是server,代表server这个fd就绪了,
            就是有活动了,什么情况下它才有活动? 当然是有新连接进来的时候呀
            新连接进来了,接受这个连接
            """
            conn, client_addr = s.accept()
            print("new connection from", client_addr)

            conn.setblocking(0)
            inputs.append(conn)
            """
            #为了不阻塞整个程序,我们不会立刻在这里开始接收客户端发来的数据, 把它放到inputs里, 下一次loop时,这个新连接
            #就会被交给select去监听,如果这个连接的客户端发来了数据 ,
            那这个连接的fd在server端就会变成就续的,select就会把这个连接返回,返回到readable 列表里,
            然后你就可以loop readable列表,取出这个连接,开始接收数据了, 下面就是这么干 的
            """
            message_queues[conn] = {"message": "", "queue": queue.Queue()}
        # 接收数据
        else:  # s不是server的话,那就只能是一个 与客户端建立的连接的fd了
            # 客户端的数据过来了,在这接收
            data = s.recv(1024)
            data = str(data, "utf-8")

            if data:
                print("收到来自[%s]的数据:" % s.getpeername()[0], data)

                message_queues[s]["message"] += data
                mowei = data[-4:]
                if mowei == zhongZhiFu:
                    message_queues[s]["message"] = message_queues[s]["message"][0:-4]
                    message_queues[s]["queue"].put(json.loads(message_queues[s]["message"]))

                    print(data)
                    if s not in outputs:
                        outputs.append(s)
                # 为了不影响处理与其它客户端的连接 , 这里不立刻返回数据给客户端

            else:  # 如果收不到data代表什么呢? 代表客户端断开了呀
                print("客户端断开了", s)

                if s in outputs:
                    outputs.remove(s)  # 清理已断开的连接

                inputs.remove(s)  # 清理已断开的连接

                del message_queues[s]  # 清理已断开的连接
    # 处理接受数据
    for s in writeable:
        try:
            next_msg = message_queues[s]["queue"].get_nowait()
            print(next_msg)
            data=None
            if next_msg["action"]=="heartbeat":
                data = heartbeat(next_msg)
            data = json.dumps(data)
            data = data.encode("utf-8")
        except queue.Empty:
            print("client [%s]" % s.getpeername()[0], "queue is empty..")
            message_queues[s]["message"]=""
            outputs.remove(s)

        else:
            # print("sending msg to [%s]" % s.getpeername()[0], data)
            s.send(data)

    for s in exeptional:
        print("handling exception for ", s.getpeername())
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        del message_queues[s]
