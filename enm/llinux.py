#!/usr/bin/python
#-*-coding:utf-8-*-
## 游标
# cusor=conn.cursor()
# cusor.execute('create database pachong;')
# cusor.execute('show databases;')
# cusor.execute('create table biaoming(name char);')
# cusor.execute('show tables;')
# print(cusor.fetchall())
# cusor.execute('show tables;')
# print(cusor.fetchall())#获取上一句sql语句执行结果
# conn.commit()#提交数据
# conn.close()#断开连接



import pymysql
class Mysql_learn(object): #obiect函数
    def __init__(self):    #init
        # 连接数据库（用来连接的）    主机号                端口号      用户           密码
        conn=pymysql.connect(host='192.168.2.114',port=3306,user='root',passwd='123456',charset='utf8')
        #设置游标(光标在什么位置在什么位置操作)
        self.su=conn.cursor()
    def cao_zuo(self):
        #执行sql语句   execute（是执行sql语句的，每次只能执行一次）
        # self.su.execute('show databases;')
        self.su.execute('use pachong;')
        # self.su.execute('show tables;')
        # fetchall 读取所有内容
        # print(self.su.fetchall())
        # fetchamany 读取多条内容  默认是第一条
        # fetchone 读取一条内容
        # print(self.su.fetchone())
        # print(self.su.fetchmany(6))
        # 提交数据,对某个表中的数据进行添加 删除和更改时使用
        # # self.coon.commit
        # for i in range(1):
        #     for j in range(100):
        #         self.su.execute('insert into  biao values ({},{});'.format(int(i),int(j)))
        # # self.coon.commit
        # self.su.execute('delete from biao;')
        # self.su.execute('select * from biao;')
        while True:
            c = input('>>>')
            self.su.execute(c)
            print(self.su.fetchall())

        # 断开连接
        # self.conn.close


    def wen_jain(self) :
        self.su.execute('use pachong;')
        self.su.execute('delete from biao;')
        with open('a.txt','r',encoding='Utf8') as a:
            c=a.readlines()
            for i in c:
                print(i.replace('\n',''))
                self.su.execute('use pachong;')
                self.su.execute('insert into  biao values ({},{});'.format(int(i),int(i)))
                self.su.execute('select * from biao;')
                print(self.su.fetchall())

    def excal(self):
        self.su.execute('use pachong;')
        self.su.execute('delete from biao;')
        import xlrd
        xl = xlrd.open_workbook('a.xls')
        sheet=xl.sheet_by_name('lbb')
        ls=sheet.ncols
        hs=sheet.nrows
        # print(ls)
        b=0
        c=[]
        for h in range(hs):
            a = 0
            for i in range(ls):
                # print(i)
                d=sheet.cell(h,a).value
                a+=1
                # print(d)
                f=['']
                if d not in f:
                    c.append(d)
        # print(c)
        for j in c:
            self.su.execute('insert into  biao values ({},{});'.format(int(j), int(j)))
            self.su.execute('select * from biao;')
            p=str(self.su.fetchall())
        return p

    # def to_txt(self,e):
        # with open('a.txt', 'a', encoding='Utf8') as a:
        #      a.write(e)

    def to_excal(self):
        import xlwt
        xl=xlwt.Workbook(encoding='UTF8')
        sheet=xl.add_sheet('lbb')
        with open('a.txt', 'r', encoding='Utf8') as f:
            b=(f.read().strip('()').replace('(','').replace(' ','').split(')'))
            # print(b)
            for i, j in enumerate(b):
                print(i, j)
                k=j.split(',')
                for h,j in enumerate(k):
                    print(h,j)
                    # sheet.write(i,h,j)
            # xl.save('a.xls')


d=Mysql_learn()
# d.cao_zuo()
# d.wen_jain()
# c=d.excal()
# d.to_txt(c)
d.to_excal()

