# coding=utf-8

import smtplib
from email.mime.text import MIMEText

# 发送纯文本格式的邮件
msg = MIMEText('人生苦短，我用Python！', 'plain', 'utf-8')

sender = 'sender@163.com'  # 发送邮箱地址

password = '123456'  # 邮箱授权码，非登陆密码！非登录密码！此处见后面讲解！

receiver = 'receiver@qq.com'  # 收件箱地址

smtp_server = 'smtp.163.com'  # smtp服务器,根据发件邮箱来设定，示例代码用的网易邮箱

msg['From'] = sender  # 发送邮箱地址

msg['To'] = receiver  # 收件箱地址

msg['Subject'] = 'from IMYalost'  # 邮件主题

smtp = smtplib.SMTP()  # 连接邮箱服务器
smtp.connect(smtp_server)

server.login(sender, password)  # 登陆邮箱

server.sendmail(sender, receiver, msg.as_string())  # 发送邮件

server.quit()  # 结束会话
login()
