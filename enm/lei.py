#!/usr/bin/python
#-*-coding:utf- 8-*-

# class Cat:
#     #属性
#     def __init__(self,newweiba,newcolour,newxinq,newwo):
#         self.weiba=newweiba
#         self.colour=newcolour
#         self.xinq=newxinq
#         self.wo=newwo
#     def __str__(self):
#         msg='有没有尾巴:'+self.weiba+'\n颜色：'+self.colour
#         return msg
#     #方法
#     # def __eat(self):
#     #     print('---吃---')
#     #     return 1
#     # def drink(self):
#     #     print('---喝---')
#     # def prinfo(self):
#     #     print(self.colour)
#     #     print(self.weiba)
#     #     print(self.wo)
#     #     print(self.xinq)
# enm=Cat('you','黑','还行','柜子')
# # # da_lao.eat()
# # da_lao.drink()
# # # da_lao.weiba='you'
# # # da_lao.colour='嗯慢，'
# # da_lao.prinfo()
# print(enm)

# class Sweetpotato:
#     def __init__(self):
#         self.cookedlevel=0
#         self.cookedString='生'
#         self.condiments=[]
#     def __str__(self):
#         msg='地瓜生熟度：'+self.cookedString+'\n地瓜的等级为：'+str(self.cookedlevel)
#         msg+='\n添加的佐料为：'
#         if len(self.condiments)>0:
#             for i in self.condiments:
#                 msg+=i+','
#             msg=msg.rstrip(',')
#         else:
#             msg='请添加佐料：'
#         return msg
#     def cook(self,times):
#         self.cookedlevel+=times
#         if self.cookedlevel>8:
#             self.cookedString='烤成木炭'
#         elif self.cookedlevel>5:
#             self.cookedString='烤好了'
#         elif self.cookedlevel>3:
#             self.cookedString='半生不熟'
#         else:
#             self.cookedString='生的'
#     def addcondiments(self,temp):
#         self.condiments.append(temp)
# digua=Sweetpotato()
# print(digua)
# digua.cook(2)
# digua.addcondiments('芥末')
# print(digua)
# digua.cook(6)
# digua.addcondiments('番茄酱')
# print(digua)
# digua.cook(2)
# print(digua)

# 继承
# class Work:
#     def hanshu(self):
#         print(245)
#     def name(self):
#         print('mingZi')
#
# class Student:
#     def hanshu(self):
#         print(12)
#     def hanshu1(self):
#         print(15241)
#     def hanshu2(self):
#         print(4563)
#
# class Kdstudent(Student,Work):
#     def __init__(self):
#         pass
# laow=Kdstudent()
# laow.hanshu2()
# laow.hanshu()
# laow.name()

# class Animal():             #统一形态
#     def talk(self):
#         pass
# class People(Animal):       #第一形态：人
#     def talk(self):
#         print('hello')
# class Pig(Animal):
#     def talk(self):
#         print('hengheng')   #第二形态：猪
# class Dog(Animal):
#     def talk(self):
#         print('wangwang')   #第三形态：狗
# People().talk()
# Dog().talk()
# Pig().talk()


# class Home():
#     def __init__(self,newarea):
#         self.area=newarea
#         self.containItems=[]
#     def __str__(self):
#         msg='家当前可用面积：'+str(self.area)+'平方米'
#         msg+='\n家里的家具有：'
#         if len(self.containItems)>0:
#             for i in self.containItems:
#                 msg+=i.name+','
#             msg=msg.strip(',')
#         else:
#             msg+='当前没有家具'
#         return msg
#     def additems(self,item):
#         if self.area>item.area:
#             self.containItems.append(item)
#             self.area-=item.area
# class Bed:
#     def __init__(self,newname,newarea):
#         self.area=newarea
#         self.name=newname
#     def __str__(self):
#         msg='床的面积为：'+str(self.area)+'平方米'
#         msg+='\n床的名字为：'+self.name
#         return msg
# class Sofa:
#     def __init__(self,newname,newarea):
#         self.area=newarea
#         self.name=newname
#     def __str__(self):
#         msg='沙发的面积为：'+str(self.area)+'平方米'
#         msg+='\n沙发的名字为：'+self.name
#         return msg
# home=Home(110)
# print(home)
# bed=Bed('席梦思',4)
# print(bed)
# home.additems(bed)
# print(home)
# bed=Bed('席梦思2',3.6)
# print(bed)
# home.additems(bed)
# print(home)
# sofa=Sofa('真皮沙发',5)
# print(sofa)
# home.additems(sofa)
# print(ho

# import xlwt    #导入xlwt模块，只有写入的权限
# xl=xlwt.Workbook(encoding='utf-8')  #写入excal文件的格式
# sheet=xl.add_sheet('python_test') #添加一个标签页（标签页的名称可以随意起）
# sheet.write(0,0,'thing')    #向标签页内写入内容，第一个，第二个(代表行或列不清楚）
# sheet.write(1,0,'nothing')  #第三个是内容
# xl.save('a.xls')#只能写.xls   但可以读.xlsx的文件


# import xlwt
# xl=xlwt.Workbook(encoding='utf-8')  #写入excal文件的格式
# sheet=xl.add_sheet('python_test')
# for i in range(1,10):
#      for j in range(1,i+1):
#          sheet.write(i-1,j-1,"%sx%s=%s"%(j,i,j*i))
# xl.save('a.xls')

# import xlrd
# xr=xlrd.open_workbook('a.xls')  #打开要操作的excal文件
''' 通过索引获取标签页'''
# b=xr.nsheets    #获取标签页个数
# print(b)
# sheet=xr.sheets()[0]   #通过索引进入要操作标签页
# hangshu=sheet.nrows     #获取标签页中的行数
# print(hangshu)

'''通过名称获取标签页'''
# name=xr.sheet_names()
# print(name)
# sheet=xr.sheet_by_name('python_test')   #通过标签页的名称进入要操作的标签页
# hangshu=sheet.nrows    #获取标签页的行数
# print(hangshu)
# hang3=sheet.row_values(2)    #获取标签页的第几行
# print(hang3)
# lieshu=sheet.ncols       #获取标签页中有多少列
# print(lieshu)
# lie3=sheet.col_values(2)    #获取标签也中的第几列
# print(lie3)
# gezi=sheet.cell(0,0).value  #获取第一个格子里的内容
# print(gezi)


# a=open('a.txt','r+',encoding='utf-8')
# from xlutils.copy import copy   #复制出来  不改变源文件  导入copy的方法
# import xlrd
# yuan_file=xlrd.open_workbook('a.xls')   #打开要操作的文件
# new_file=copy(yuan_file)        #复制文件，并不会写入源文件里，而是复制的一份新文件再操作，只有写入功能，没有读取功能
# sheet=new_file.get_sheet(0)     #获取要操作的标签页，get_sheet(下标位置)
# sheet.write(0,0,'{}'.format(a))
# new_file.save('a.xls')

# import time
# a=time.strftime('%Y-%m-%d %H:%M:%S:%W',time.localtime(2000))
# print(a)

import time
# a=(2019,7,1,16,27,3,1,231,14)
# b=time.mktime(a)
# print(b)
# print(time.strftime('%Y-%m-%d %H:%M:%S:%W',time.localtime(2000)))#将结构化时间转换为格式化时间
# print(time.strptime('2019/09/19 10:05:28','%Y/%m/%d %X'))#将格式化时间转换为结构化时间
# import time
# from time import sleep
# start = time.time()
# for i in range(3):
#     sleep(2)
#     print(i)
# end=time.time()
# print(end-start)

# a=[]
# b=[11,2,3,5]
# a.append(b[2])
# print(a)
# a.append(b[3])
# time.sleep(5)
# print(a)


import re
import requests


class Douban(object):
    def qing_qiu(self, page):
        url = f'https://movie.douban.com/top250?start={page}&filter='
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
        }
        # 发送请求，并将结果赋值给res
        res = requests.get(url=url, headers=head)
        # 读取结果
        h = res.content.decode('utf-8')
        return h

    def guo_lv(self, html):
        patt = re.compile(r'<span class="title">(.*?)</span>', re.S)
        items = patt.findall(html)

        for i in items:
            if '&nbsp' in i:
                items.remove(i)
        return items

    def save(self, shuju):
        with open('a.txt', 'a', encoding='utf-8') as f:
            for i in shuju:
                f.write(i + '\n')


dd = Douban()
for i in range(25, 100, 25):
    hh = dd.qing_qiu(i)
    shuju = dd.guo_lv(hh)
    dd.save(shuju)