import selectors
import socket,json

Androids={}#安卓连接设备列表

sel = selectors.DefaultSelector()
print(type(sel))
def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        # print('echoing', repr(data), 'to', conn)
        data_json=json.loads(str(data,encoding="utf-8"))#将收到的数据转为json格式
        linkID=data_json["id"]
        # print(linkID)
        if linkID=='123456':
            Androids[conn]=linkID
            print(Androids[conn])
            print(Androids)

        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('192.168.171.1', 9999))
sock.listen(1000)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)