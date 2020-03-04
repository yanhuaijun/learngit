import requests
import json


# def get_access_token():
#     """
#     获取微信全局接口的凭证(默认有效期俩个小时)
#     如果不每天请求次数过多, 通过设置缓存即可
#     """
#     result = requests.get(
#         url="https://api.weixin.qq.com/cgi-bin/token",
#         params={
#             "grant_type": "client_credential",
#             "appid": "wx87d17a791d346b6b",      #wx2499da7621f818e8
#             "secret": "8d2d3270d9c8c564056dbe43110a7dce",   #6239e3dfc5af686777ea40b9f3df5f48
#         }
#     ).json()
#
#     if result.get("access_token"):
#         access_token = result.get('access_token')
#     else:
#         access_token = None
#     return access_token
# access_token = get_access_token()

# print(access_token)
access_token='23_eb-XWhcZjEIxSilpAyVhsAJgB3e292Kwl0VISfZoY2HUToJdtG6WdapPm51MaXbXD8d3hiCxgk8aoc4kKx5ZKd4WP-rxZe54pn4MtQdaYaGQdhXUZfqg_rKxD9ehCu0VK_sKrlgpMRx85nWYXHCeABAQAV'
def sendmsg(openid,msg):

    #access_token = get_access_token()

    body = {
        "touser": openid,
        "msgtype": "text",
        "text": {
            "content": msg
        }
    }
    response = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
        params={
            'access_token': access_token
        },
        data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
    )
    # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
    result = response.json()
    print(result)

sendmsg('oj9C-5mbbEk4R534kDXqotqiqYfM','今天是不是很忙呀！')
# 	 oj9C-5uMzW9agerUMkcuNFCjCD1M
# if __name__ == '__main__':