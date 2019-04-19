import json,time,socket

class SocketClient(socket.socket):
    def __init__(self,id=None):
        socket.socket.__init__(self,family=2, type=1, proto=0, fileno=None)
        self.id=id

    def readM(self):
        data = self.recv(1024)
        data=str(data,encoding="utf-8")
        data = json.dumps(data)
        return data

    def sendM(self,data):
        data=json.loads(data)
        data=data.encode("utf-8")
        self.send(data)

    def heartbeat(self,data):
        time.sleep(10)
        self.send(data)

class manage():
    def __init__(self,r,s=None):
        self.requestsManage=r
        self.sendManage=s


    def serializeJson(self):
        d=json.dumps(self.requestsManage)
        return d

    def deSerializeJson(self):
        d=json.loads(self.sendManage)
        return d

m=socket.socket

if __name__ == '__main__':
    s=SocketClient(1)
    print(type(s))
    print(s.id)