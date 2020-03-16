from django.shortcuts import render
from werobot import WeRoBot
import hashlib,requests
from .models import *
from django.shortcuts import render ,HttpResponse,redirect
import urllib.parse as urlparse  #解析URL
'''
render   #向浏览器返回页面
HttpResponse   #向浏览器返回字符内容
redirect   #重定向
'''
# Create your views here.
def check(request):
        print('微信token验证')
        wechat_data = request.GET
        signature = wechat_data['signature']
        timestamp = wechat_data['timestamp']
        nonce = wechat_data['nonce']
        echostr = wechat_data['echostr']
        token = 'yanhuaijuntest'

        check_list = [token, timestamp, nonce]
        check_list.sort()
        s1 = hashlib.sha1()
        s1.update(''.join(check_list).encode())
        hashcode = s1.hexdigest()
        print("handle/GET func: hashcode, signature:{0} {1}".format(hashcode, signature))
        if hashcode == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("重新验证token")

def wxindex(requests):
        return render(requests,'wxindex.html')
def gzhuweixin(requests):
        return render(requests,'gzhuweixin.html')



APPID = 'wx87d17a791d346b6b'  # 公众号ID
APPSECRET = '8d2d3270d9c8c564056dbe43110a7dce'  # 公众号密钥
REDIRECT_URI = 'http://cn5.mx5180.com/web/haha/'  #http://127.0.0.1:8000/wx/wxindex/'#'  # 回调URL，需要在公众号中配置
SCOPE = 'snsapi_userinfo'  # 弹出授权页面，可通过openid拿到昵称、性别、所在地。并且， 即使在未关注的情况下，只要用户授权，也能获取其信息

'''
1.页面调授权接口重定向 到获取用户信息接口
2.获取用户信息完之后 再返回页面
'''
def userinfor(request):
        print('微信授权')# 第一步：后端重定位到微信提供的接口URL，让用户同意授权后，微信服务器会跳转到回调地址并携带code参数
        source_url = 'https://open.weixin.qq.com/connect/oauth2/authorize' \
                     + '?appid={APPID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={SCOPE}' \
                     + '#wechat_redirect'
        url = source_url.format(APPID=APPID, REDIRECT_URI=REDIRECT_URI, SCOPE=SCOPE)
        print(url)
        return redirect(url)  # 重定向
def hahaindex(request):
        if request.method == 'GET':
                print(request.GET.get)
                code = request.GET.get('code')
                print(code)
                # return HttpResponse('获取用户信息')

                source_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?' \
                             + 'appid={APPID}&secret={APPSECRET}&code={CODE}&grant_type=authorization_code'
                access_token_url = source_url.format(APPID=APPID, APPSECRET=APPSECRET, CODE=code)
                resp = requests.get(access_token_url)
                data = eval(resp.text)  # 将字符串转为字典
                print(data)
                # access_token = data['access_token']
                openid = data['openid']
                print(openid)
                if openid:
                        try:
                                user = wxuser.objects.get(openid=openid)
                                print(user)
                                return redirect('/wx/wxindex.html/')
                        except:  # 如果用户不存在，提交到数据库保存
                                return redirect('/wx/gzhuweixin.html',{'message':'请先关注公众号'})
                else:
                        # message = "用户名或密码为空！请重新输入！"
                        return "请刷新页面，再试一次！"

        # # 第四步：拉取用户信息(需scope为 snsapi_userinfo)
        # source_url = 'https://api.weixin.qq.com/sns/userinfo' \
        #              + '?access_token={ACCESS_TOKEN}&openid={OPENID}&lang=zh_CN'
        # useinfo_url = source_url.format(ACCESS_TOKEN=access_token, OPENID=openid)
        # resp = requests.get(useinfo_url)
        # data = eval(resp.text)
        # print(data)
        # userinfo = {
        #         'nickname': data['nickname'],
        #         'sex': data['sex'],
        #         'province': data['province'],
        #         'city': data['city'],
        #         'country': data['country'],
        #         'headimgurl': data['headimgurl']
        # }
