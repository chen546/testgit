#!/usr/bin/python
#-*-coding:utf-8-*-

import smtplib               #封装smtp协议
import email.mime.text       #处理正文中的数据的
import email.mime.multipart  #邮件的格式

sender = '15039008093@163.com'
reser = ['l13812929932@163.com','l13723282692@163.com','mc1832713135@163.com']
server = 'smtp.163.com'
# 授权码   通过代码发送邮件 需要服务器授权
passwd='2436jin'
message=email.mime.multipart.MIMEMultipart()
message['from']=sender
message['TO']=''.join(reser)
message['subject']='python_learn'
aa="""纳税了吗
"""
txt=email.mime.text.MIMEText(aa)

# 将正文添加到邮件里  附属（attach）
message.attach(txt)

# 定义发送的附件的文件名，文件可以说任意格式的
att1=email.mime.text.MIMEText(open('a.txt','rb').read(),'base64','utf-8')

# 附件携带的字段和值
att1["Content-Type"]='application/octet-stream'

#附件携带的字段和值 这里的filename可以任意写，写什么名字，邮件里附件就是什么名字
att1["Content-Disposition"]='attachment；filename="sqhy.txt"'

# 附件添加到邮件
message.attach(att1)
# 定义发送邮件的服务器和端口号
smtp123=smtplib.SMTP_SSL(server,465)
smtp123.login(sender,passwd)
# 发送邮件          发送者 接收者   发送的内容（必须处理成txt文件）
smtp123.sendmail(sender,reser,message.as_string())
# 断开连接
smtp123.close()
