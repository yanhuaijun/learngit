# -*- coding:utf-8 -*-微信公众号天气、区号、邮政编码返回、匹配什么返回什么
import werobot
import re
import pymysql,json,requests
import flask


# robot = werobot.WeRoBot(token='yanhuaijun')

# @robot.handler
def echo(message):
    return 'Hello World!'

#阿里云数据库
def my_db(msg):
    conn = pymysql.Connect(
        host='47.106.143.70',##mysql服务器地址
        port=3306,##mysql服务器端口号
        user='yhj666',##用户名
        passwd='aa123456',##密码  J5p";~OVazNl%y)?
        db='yhj666',##数据库名
        charset='utf8',##连接编码
    )

    # cursor = con.cursor()  # 获取游标
    sq1 = 'SELECT * FROM cityid WHERE city_name LIKE "%s"' % ('%' + msg + '%')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sq1)
    uer = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return uer


def tqyb(uer):
    url1 = "http://t.weather.sojson.com/api/weather/city/" + uer['city_code']
    re = requests.get(url1)
    tq0 = re.json()["cityInfo"]
    tq = re.json()["data"]["forecast"][0]
    tq1 = re.json()["data"]
    # print("当前城市:"+tq0["parent"],tq0["city"])
    tq00 = "当前城市:" + tq0["parent"], tq0["city"], "今天" + tq["week"], "最" + tq["high"], "最" + tq["low"]\
        , "天气类型:" + tq["type"], tq["fx"], tq["fl"], "温馨提示：" + tq["notice"]\
        , "湿度:" + tq1["shidu"], "空气质量:" + tq1["quality"], "感冒指数:" + tq1["ganmao"], "天气更新时间:" + tq0["updateTime"]
    # print(tq00)
    return tq00

msg1='广州区号'
msg=msg1[0:2]
uer = my_db(msg)
print(uer)
# print(tq00)
# return tq00
# 解析消息
def mensg():
    tq00 = tqyb(uer)
    if uer:
        if '区号'in msg1:
            if uer['area_code']=='NULL':
                return '客官别急，数据正在补齐中....请谅解'
            else:
                qh=msg+'的区号为:'+uer['area_code']
                return qh
        elif '编码'in msg1:
            if uer['area_code']=='NULL':
                return '客官别急，数据正在补齐中....请谅解'
            else:
                bm=msg+'邮政编码为:'+uer['post_code']
                return bm
        else:
            print(uer['city_code'])
            return tq00
    else:
        return '输入有误'

print(mensg())



# server=flask.Flask(__name__)
# @server.route('/login',methods=['get'])#登录函数
# def login():
#     username=flask.request.values.get('username')
#     passwd=flask.request.values.get('passwd')
#     if username :
#         sql='select * from cityid where city_name LIKE "%s" ;'%(username)
#         uer=my_db(sql)
#         print(uer)
#         print(sql)
#         if uer:
#             res = {'msg': '欢迎你，登录成功！', 'msg_code': 2001}
#         else:
#             # sql='INSERT INTO`my_user`(`username`, `passwd`, `is_admin`) VALUES("%s","%s",0);'%(username,passwd)
#             # my_db(sql)
#             res={'msg':'用户名密码错误！','msg_code':10001}
#     else:
#         res={'msg':'参数错误，请联系管理员！','msg_code':1001} #1001表示必填接口未填
#     return json.dumps(res,ensure_ascii=False)
# server.run(port=8087,debug=True,host='0.0.0.0')

#
# @robot.text
# def echo(message):
#     # try:
#     #     # 提取消息  city_name LIKE '%广州%'
#     #     msg = message.content.strip().lower().encode('utf8')
#         # 解析消息
#         msg=message.content
#         if msg:
#             sql = 'select * from my_user where city_name LIKE "%s";' % msg
#
#
#             uer = my_db(sql)
#             print(sql)
#         if  re.compile(".*?你好.*?").match(msg) or\
#             re.compile(".*?嗨.*?").match(msg) or\
#             re.compile(".*?哈喽.*?").match(msg) or\
#             re.compile(".*?hello.*?").match(msg) or\
#             re.compile(".*?hi.*?").match(msg) or\
#             re.compile(".*?who are you.*?").match(msg) or\
#             re.compile(".*?你是谁.*?").match(msg) or\
#             re.compile(".*?你的名字.*?").match(msg) or\
#             re.compile(".*?什么名字.*?").match(msg) :
#             return "你好~\n我是呓语的管家机器人，主人还没给我起名字 T_T\n有什么能帮您的吗？（绅士脸）"
#         elif re.compile(".*?厉害.*?").match(msg):
#             return '承让承让 (๑•̀ㅂ•́)ﻭ✧'
#         elif re.compile(".*?想你.*?").match(msg):
#             return '我也想你'
#         elif re.compile(".*?miss you.*?").match(msg):
#             return 'I miss you,too'
#         elif re.compile(".*?我爱你.*?").match(msg):
#             return '我也爱你'
#         elif re.compile(".*?love you.*?").match(msg):
#             return 'I love you,too'
#         elif re.compile(".*?美女.*?").match(msg):
#             return '我是男生哦♂'
#         elif re.compile(".*?帅哥.*?").match(msg):
#             return '谢谢夸奖 (๑•̀ㅂ•́)ﻭ✧'
#         elif re.compile(".*?傻逼.*?").match(msg):
#             return '爸爸不想理你'
#         else:
#             return '噢，抱歉，没有你想要的结果！'
#     # except Exception as e:
#     #     print (e)
#     #
#
#
# robot.config['HOST'] = '0.0.0.0'
# robot.config['PORT'] = 80
#
# robot.run()
