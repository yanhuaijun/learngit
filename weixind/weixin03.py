import csv
from wxpy import *
import time

# 运行代码之前需要先将表格里的姓名换成你的朋友的微信名字。

def read_info():
    f = open(r'E:\BaiduNetdiskDownload/sample.csv','r',encoding='gbk')
    reader = csv.DictReader(f)
    return [info for info in reader]#[{},{},{}]

    #'xx-同学请于 xx 时间参加 xx 课程，课程地址是 xxx。收到请回复，谢谢'
def make_msg(raw_info):
    t = '{n}-同学请于{t}时间参加{s}课程，课程地址是{a}。收到请回复，谢谢!'
    return [t.format(n=info['姓名'],
                     t=info['上课时间'],
                     s=info['课程'],
                     a=info['上课地址']
                     ) for info in raw_info]
    # -> list ['xxx','xxx']
def send(msg_list):
    bot = Bot()
    for msg in msg_list:
        fren_name = msg.split('-')[0]
        f = bot.friends().search(fren_name) # list
        if len(f) == 1:
            f[0].send(msg)
        else:
            print(fren_name)
            print('Please check this name')
    time.sleep(5)

if __name__ == '__main__':
    raw_info = read_info()
    msg_list = make_msg(raw_info)
    send(msg_list)