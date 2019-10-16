#!/usr/bin/python
#-*-coding:utf-8-*-
# import pymysql
# class SA:
#     def __init__(self):
#         conn=pymysql.connect(host='192.168.2.114',port=3306,user='root',passwd='123456',charset='utf8')
#         self.su=conn.cursor()
#
#
#
# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
# s=0
# su=0
# b=[]
# n=int(input('n='))
# a=int(input('a='))
# for i in range(1,n+1):
#     s=a+s
#     a=a*10
#     b.append(s)
#     print(s)
# for i in b:
#     su+=i
# print(su)

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# su=100
# a=100
# for i in range(1,11):
#     a=a/2
#     print(a)
#     su+=2*a
#     # print(su)
#     if i==10:
#         print('第十次：{}'.format(a))
#         print(su)

# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# a = 2.0
# b = 1.0
# s = 0
# for n in range(1,21):
#     s += a / b
#     t = a
#     a = a + b
#     b = t
# print(s)

a=1
b=2
s=[]
while a<=100:
    a+=1
    print(a)
    while b<=a:
        if a%b==0:
            break
        else:
            s.append(a)
print(s)






