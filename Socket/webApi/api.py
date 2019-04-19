# 客户端请求网站-阻塞实现（一次一次的请求)
import socket
import time

# 访问网站
ACCESS_URL = 'www.baidu.com'
# 端口
ACCESS_PORT = 80


# socket阻塞请求网站
def blocking(pn):
    sock = socket.socket()
    sock.connect((ACCESS_URL, ACCESS_PORT))  # 连接网站 ，发出一个HTTP请求
    request_url = 'GET {} HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(pn))
    print(request_url)
    sock.send(request_url.encode())
    response = b''
    chunk = sock.recv(1024)
    while chunk:  # 循环接收数据，因为一次接收不完整
        response += chunk
        chunk = sock.recv(1024)
    # print(response.decode())
    return response


def block_way():
    for i in range(5):
        blocking(i)


if __name__ == '__main__':
    # start = time.time()
    # # block_way()
    # print('请求5次页面耗时{}'.format(time.time() - start))
    # """
    # 请求5次页面耗时2.4048924446105957
    # """
    ACCESS_URL = 'www.kuaidaili.com'
    sock = socket.socket()
    sock.connect((ACCESS_URL, ACCESS_PORT))
    request_url = 'GET {} HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(1))
    print(request_url)
    request_url = "HTTP/1.0\r\nwww.kuaidaili.com/free/inha/1/\r\n\r\n"
    print(request_url)
    sock.send(request_url.encode())
    response = b''
    chunk = sock.recv(1024)
    while chunk:  # 循环接收数据，因为一次接收不完整
        response += chunk
        print(response.decode("utf8"))
        chunk = sock.recv(1024)

    # print(response)
