# 不要抄下源码就运行，你需要改动几个地方

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import time
import itchat

bot = Bot()

# linux执行登陆请调用下面的这句
# bot = Bot(console_qr=2,cache_path="botoo.pkl")



# 机器人账号自身
myself = bot.self

# 向文件传输助手发送消息
bot.file_helper.send('Hello from wxpy!')

# # 在 Web 微信中把自己加为好友
# bot.self.add()
# bot.self.accept()
#
# # 发送消息给自己
# bot.self.send('能收到吗？')

# print(Bot.user_details('user_or_users', chunk_size=50))
# Bot.friends(update=False)
# # 搜索名称包含 '游否' 的深圳男性好友
# found = bot.friends().search('晓军')
# # [<Friend: 游否>]
# # 确保搜索结果是唯一的，并取出唯一结果
# youfou = ensure_one(found)
# # <Friend: 游否>
my_friend=bot.friends().search(u"晓军")[0]
my_friend.send('Hello, WeChat!')

time.sleep(2)
my_friend=bot.friends().clear()
my_friend=bot.friends().search("u贰B")[0]
my_friend.send('Hello, WeChat!')




def get_news():
    """获取金山词霸每日一句，英文和翻译"""

    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note




# friends = itchat.get_friends()
# for i in range(0,5):
#     print(friends[i])
    # if "晓军" in friends[i]["NickName"]:
    #     print(friends[i])
    #     print(i)
    #     # itchat.send("你还要多久才能下班", toUserName=friends[i]['UserName'])
    #
    #
    # elif "敬畏" in friends[i]["NickName"]:
    #     print(friends[i])
    #     print(i)
    #     # itchat.send("测试测试", toUserName=friends[i]['UserName'])


# def send_news():
#
#     try:
#         list=["发福的","晓军"]
#
#         content,note = get_news()
#         for i in list:
#             print(i)
#             # 你朋友的微信名称，不是备注，也不是微信帐号。
#             my_friend = bot.friends().search(i)[0]
#             my_friend.send(content)
#             my_friend.send(note)
#
#             # my_friend.send("456")
#             # my_friend.send("123")
#             my_friend.send(u"Have a good one!")
#             time.sleep(2)
#         send_news()
#
#         # my_friend = bot.friends().search(u'晓军')[0]
#         # my_friend.send("456")
#         # my_friend.send("123")
#         # send_news()
#         # time.sleep(10)
#         # 每86400秒（1天），发送1次
#         # t = Timer(20, send_news)
#         # t.start()
#     except:
#
#         # 你的微信名称，不是微信帐号。
#
#         my_friend = bot.friends().search('发福的')
#         #my_friend.send(u"今天消息发送失败了")


# if __name__ == "__main__":
#     send_news()