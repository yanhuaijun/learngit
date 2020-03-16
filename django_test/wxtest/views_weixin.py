#微信函数分享
from django.shortcuts import render,HttpResponse,redirect
import json,urllib,requests,time,os,random,hashlib

'''
3月16新增微信分享设置
'''
#微信API信息
WEIXINAPI = {
    "tokenUrl": "https://api.weixin.qq.com/cgi-bin/token?",
    "ticketUrl": "https://api.weixin.qq.com/cgi-bin/ticket/getticket?",
    "appID": "wx87d17a791d346b6b",
    "appwd": "8d2d3270d9c8c564056dbe43110a7dce"
}

#分享页面信息
PAGEINFO = {
    "Title": "1这里是标题信息",
    "Description": "这里是描述信息2",
    "PicUrl": "3这里是你要分享的url"
}
#获取token
# def flush_token():
#     token_url = WEIXINAPI["tokenUrl"]
#     appID = WEIXINAPI["appID"]
#     appwd = WEIXINAPI["appwd"]
#     url = "%sgrant_type=client_credential&appid=%s&secret=%s" % (token_url, appID, appwd)
#     jsondata = urllib.request.urlopen(url).read().decode()
#     json_dic = json.loads(jsondata)
#     return json_dic["access_token"]
# print(flush_token())


access_token1='31_2PYVgYYlmhvmbM1vRQ6RJ-G6NIihqQG4Suqu_uRao209hM-_-VfpS8CRfd6ePu_7HclUTZLa6Mml3bPQgsoXcFOCv_yfWeJ8mX1h-hwVrLBmNqq1nzuzVqF9FygcfLkYjDX7KlKbufoLXp62MMNhAIAHHI'
#通过token获取 ticket
def flush_ticket(access_token):
    ticket_url = WEIXINAPI["ticketUrl"]
    url = '%saccess_token=%s&type=jsapi' % (ticket_url, access_token)
    jsondata = urllib.request.urlopen(url).read().decode()
    json_dic = json.loads(jsondata)
    json_dic["expires_time"] = time.time()
    with open("ticket.txt", 'w') as f:
        json.dump(json_dic, f)
    return json_dic["ticket"]

#ticket如果超过两个小时了，需要更新；没有超过，则直接使用
def get_ticket():
    if os.path.exists("ticket.txt"):
        with open('ticket.txt', 'r') as f:
            ticket_dic = json.load(f)
        expires_time = ticket_dic['expires_time']
        now_time = time.time()
        if now_time - expires_time >= 7200:
            #更新ticket
            access_token = access_token1
            ticket = flush_ticket(access_token)
        else:
            ticket = ticket_dic["ticket"]
    else:
        access_token = access_token1
        ticket = flush_ticket(access_token)
    return ticket
print(get_ticket())

#生成随机数
def randomone(n):
    string = ''
    if n.isdigit():
        for i in range(int(n)):
            if i%2 != 0:
                tmp = random.randint(0,9)
            else:
                tmp = str(chr(random.randint(97, 122)))
            string = "%s%s" % (string, tmp)
    return string

#生成签名
def create_string(url):
    random_string = randomone('16')
    times = int(time.time()/1000)
    ticket = get_ticket()
    arg_string = "jsapi_ticket=%s&noncestr=%s&timestamp=%s&url=%s" % (ticket, random_string, times, url)
    m = hashlib.sha1()
    m.update(arg_string.encode('utf8'))
    sign = m.hexdigest()
    return times,random_string,sign

#返回页面
def index(request):
    url = request.get_host() + request.get_full_path()
    url = 'http://%s' % url
    appId = WEIXINAPI["appID"]
    timestamp, nonceStr, signature = create_string(url)
    title = PAGEINFO["Title"]
    des = PAGEINFO["Description"]
    picture = PAGEINFO["PicUrl"]
    return render(request, 'weixinindex.html', locals())