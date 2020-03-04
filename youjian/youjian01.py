#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from requestsZ.requests01 import post1

# yy=post1("13066875865","aa123456","aa1234560").text
# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "563292370@qq.com"  # 用户名
mail_pass = "ycolojpjejilbchd"  # 口令

sender = '563292370@qq.com'
receivers = ['563292370@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱 ,'710102624@qq.com'  497756299,'497756299@qq.com'


message = MIMEText('亲爱的，你晚上要加班吧，辛苦啦！么么哒！', 'plain', 'utf-8')
message['From'] = Header("菜鸟Python", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")