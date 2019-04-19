import socket, select, queue

host = "192.168.171.1"
port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen(100)
print("正在监听...........")
inputs = [server]
outputs = []

msg_dic = {}

while True:
    readyInput, readyOutput, readyException = select.select(inputs, outputs, inputs)
    for r in readyInput:
        if r is server:
            conn, addr = server.accept()  # conn新连接
            inputs.append(conn)
            print(conn, "\n", addr)
            msg_dic[conn] = queue.Queue()
        else:
            data = r.recv(1024)
            print(data)
            msg_dic[r].put(data)
            outputs.append(r)

    for o in readyOutput:
        data_to_llect = msg_dic[o].get()
        o.send(data_to_llect)

        outputs.remove(o)

    # 处理断开的连接
    for e in readyException:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dic[e]
