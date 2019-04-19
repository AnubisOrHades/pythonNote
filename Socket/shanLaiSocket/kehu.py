import socket,time
import sys
#
# # 创建 socket 对象
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 获取本地主机名
# host = socket.gethostname()
#
# # 设置端口号
# port = 9999
#
# # 连接服务，指定主机和端口
# s.connect((host, port))
# try:
#     i=1
#     while 1:
#         # 接收小于 1024 字节的数据
#         msg = s.recv(1024)
#         if msg!=0:
#             print (msg.decode('utf-8'))
#             time.sleep(8)
#         i+=1
#         print(i)
# except:
#     s.close()
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.171.1", 9999))
