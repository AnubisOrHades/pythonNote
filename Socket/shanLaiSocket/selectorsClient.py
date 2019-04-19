# _*_coding:utf-8_*_
__author__ = 'Alex Li'

import socket
import sys

#  b'This is the message/r/t',
#              b'It will be sent/r/t',
#              b'in parts/r/t',
messages = [
    '{"id":"123456","uniqueId":"1bd06403-31b9-476f-ad03-722820","action":"heartbeat","messageId":"123456","data":{"昊天"}}/r/t',

    '{"id":"999999","uniqueId":"1bd06403-31b9-476f-ad03-722820","action":"heartbeat","messageId":"123456","data":{}}/r/t'
]
server_address = ('192.168.171.1', 9999)

# Create a TCP/IP socket
socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(100)]
print(len(socks), socks)
# Connect the socket to the port where the server is listening
print('connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)

for message in messages:

    # Send messages on both sockets
    for s in socks:
        print('%s: sending "%s"' % (s.getsockname(), message))
        s.send(message.encode("utf-8"))

    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print('%s: received "%s"' % (s.getsockname(), data))
        if not data:
            print('closing socket', s.getsockname())
