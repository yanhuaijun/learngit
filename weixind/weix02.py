import itchat

from wxpy import *

# bot = Bot()
itchat.auto_login(hotReload=True)

friends = itchat.get_friends()


list=[234,]

# print(friends[3])
for i in range(0,300):
    if "晓军" in friends[i]["NickName"]:
        print(friends[i])
        print(i)
        # itchat.send("你还要多久才能下班", toUserName=friends[i]['UserName'])


    elif "敬畏" in friends[i]["NickName"]:
        print(friends[i])
        print(i)
        # itchat.send("测试测试", toUserName=friends[i]['UserName'])

# itchat.send("测试测试", toUserName=friends[0]['UserName'])
# itchat.send("测试测试", toUserName=friends[2]['UserName'])

