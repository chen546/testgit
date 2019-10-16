#!/usr/bin/python
#-*-coding:utf-8-*-
import socket
while True:
    # 创建一个套件
    sock=socket.socket()
    # 客户端虽然不需要绑定ip  但是连接服务器
    sock.connect(('192.168.2.116',88))
    # 发送请求
    # 输入请求的内容
    message=input('请输入请求的内容:')
    # 发送请求的内容给服务器
    sock.send(message.encode('utf-8'))
    # 接受服务器的响应
    recive=sock.recv(1024)
    print(recive.decode('utf-8'))
    # 断开连接
    sock.close()
