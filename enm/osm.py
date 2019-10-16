#!/usr/bin/python
#-*-coding:utf-8-*-
import os

# popen()执行cmd命令
# a=os.popen('nslookup www.baidu.com')
# print(a.read())

# 获取当前所在目录
# print(os.getcwd())

# chdir切换目录
# os.chdir('../..')
# print(os.getcwd())

# 创建目录
# os.mkdir('aaa')
# 创建递归目录
# os.makedirs('a/b/c')
# 删除递归目录
# os.removedirs('a/b/c')
# 删除空目录
# os.rmdir('aaa')
# 删除文件
# os.remove('222.txt')
# 文件重命名
# os.rename('daoru.py','llinux.py')
# 获取目录下的所有文件
# print(os.listdir('D:\pycharm'))
# 将文件名与路径分隔开
# aa=os.path.split(r'd:\pycharm\chen')
# print(aa)
# 判断是否是目录
# aa=os.path.isdir(r'wenjian.py')
# print(aa)
# 判断是否是文件
# aa=os.path.isfile(r'wenjian.py')
# print(aa)

# 统计当前目录下有多少目录文件和普通文件
# aa=os.listdir('D:\pycharm\enm')
# a=0
# b=0
# for i in os.listdir('D:\pycharm\enm'):
#     if os.path.isdir(i):
#         b+=1
#     if os.path.isfile(i):
#         a+=1
# print('目录文件：{}'.format(b))
# print('普通文件：{}'.format(a))

# aa=[print(a,b)   for i in os.listdir('D:\pycharm\enm')  if os.path.isdir(i) b+=1 if os.path.isfile(i) a+=1]
# import time
# year = int(input("输入一个年份: "))
# m =int(input("请输入月："+'\n'))
# day=int(input("请输入日："+'\n'))
# a='{},{},{}'.format(year,m,day)
# print(a)
#
# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
#        else:
#            print("{0} 不是闰年".format(year))
#    else:
#        print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
# else:
#    print("{0} 不是闰年".format(year))
#
# mouth_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
#     mouth_day[1] = 29
# print('今天是第{}天'.format(sum(mouth_day[:m-1])+day))


# 用于远程控制
import paramiko
# 创建一个ssh客户端   类似xshall
# ssh123=paramiko.SSHClient()
# # 将第一次连接到的主机添加跳过验证，并添加到know_host文件中（存放的是可以远程的主机的地址）
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# ssh123.connect(hostname='192.168.2.155',port=22,username='root',password='123456')
# # stouin:指的是输入的命令,必须是有结果的命令。stuout：指的是输出的结果,stuerr：命令的报错
# stouin,stuout,stuerr=ssh123.exec_command('pwd')
# aa=stuout.read().decode('utf-8')
# print(aa)
#
# #断开连接
# ssh123.close()

# 使用sftpclinet组件传输文件
# # 1 建立一个传输通道，填入ip地址和端口号（是一个元组）
# transport=paramiko.Transport(('192.168.2.137',22))
# # 2 连接主机，只需要输入用户名和密码
# transport.connect(username='root',password='123456')
# # 3 创建一个sftp客户端
# sftp_clinet=paramiko.SFTPClient.from_transport(transport)
# # 4从Linux下载文件到windows
# # sftp_clinet.get('/home/enm/桌面/a.txt',r'D:\pycharm\chen\gy.txt')
# # 5 从windows上传文件到Linux
# sftp_clinet.put(r'D:\pycharm\chen\gy.txt','/home/enm/桌面/c.txt')
#

# import paramiko
# ssh=paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh.connect(hostname='192.168.2.137',port=22,username='root',password='123456')
# stouin,stuout,stuerr=ssh.exec_command('ifconfig')
# aa=stuout.read().decode('utf-8')
# print(aa)



