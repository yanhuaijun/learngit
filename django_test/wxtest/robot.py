# coding=utf8 微信公众号代码
from werobot import WeRoBot
from .models import *
import time
robot = WeRoBot(enable_session=False,
                token='yanhuaijuntest',
                app_id='wx87d17a791d346b6b',
                app_secret='8d2d3270d9c8c564056dbe43110a7dce', )


# @robot.handler
# def hello(message):
#     return "hello world! yhj888"

@robot.key_click("music")
def music(message):
    return '你点击了“今日歌曲”按钮'

@robot.subscribe
def subscribe(message):
    print('关注信息')
    print(message.FromUserName)
    openid=message.FromUserName
    createtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    upeate_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if openid:
        try:
            user = wxuser.objects.get(openid=openid)
            print(user)
            user.stats = '1'
            user.upeate_time=upeate_time
            user.save()
            return "欢迎再次关注！"
        except:  # 如果用户不存在，提交到数据库保存
                re1 = wxuser.objects.create(openid=openid, create_time=createtime,stats=1,upeate_time=upeate_time)
                re1.save()
                return "终于等到你，欢迎关注！"
    else:
        # message = "用户名或密码为空！请重新输入！"
        return "警告，非法请求！"
@robot.unsubscribe
def unsubscribe(message):
    print('取消关注')
    # print(message.FromUserName)
    openid=message.FromUserName
    createtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    upeate_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        user = wxuser.objects.get(openid=openid)
        user.stats = '0'
        user.upeate_time=upeate_time
        user.save()
        return "欢迎你的再次光临！"
    except:

            return "请先关注公众号！"

@robot.text
def echo(message):
    #try:
        # 提取消息
        msg1 = message.content
        print('文本'+msg1)
        return msg1

@robot.image
def img(message):
    # print(type(message))
    # print(type(message.img))
    # return message.img
    return "别闹，还是发文字吧!"


@robot.voice
def voice(message):
    return "有什么心里话，可以微我。"


@robot.video
def video(message):
    return "抱歉我看不懂视频！可以给我主人发哦"


@robot.link
def link(message):
    return "抱歉我打不开链接，你可以告诉我里面的故事啊！"


@robot.unknown
def unknown(message):
    return "可以好好说话吗？"
