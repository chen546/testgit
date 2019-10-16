#!/usr/bin/python
#-*-coding:utf-8-*-
import socket
# socket本机自带的模块  作用：socket:套接字，封装的源端口号，目的端口号，源ip，目的ip。提供的是通信双方通信的功能
# tcp协议 通信        服务器端
# 创建一个套接字（创建一个有接受能力和发送能力的对象）
# AF-INET：代表ipv4
# SOCK_STREAM   tcp套接字类型
# sock_DGRAM    udp套接字类型

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip地址和端口号
s.bind(('192.168.2.116',88))
# 监听，启用服务器以接受连接
s.listen(3)
while True:
    # 接收请求
    #第一个值  建立连接的信息    第二个值  客户端的ip地址和端口号
    client,addr=s.accept()
    # 接受客户端发送的请求最大值是1024字节
    recive=client.recv(1024)
    # 将接受过来的信息解码打印
    print(recive.decode('utf-8'))
    # 发送响应  输入响应内容

    reponse=input('请响应：')
#     将输入的响应内容发送
    client.send(reponse.encode('utf-8'))