# -*- coding:utf-8 -*-

from flask import Flask,request
from time import time
import xml.etree.ElementTree as et
import hashlib
import requests
import json

app = Flask(__name__)
app.debug = True



@app.route('/wx',methods=['GET','POST'])
def wechat():

    if request.method == 'GET':
        token = 'yanhuaijun'
        data = request.args
        signature = data.get('signature','')
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')

        list = [token, timestamp, nonce]
        list.sort()

        s = list[0] + list[1] + list[2]

        hascode = hashlib.sha1(s.encode('utf-8')).hexdigest()

        if hascode == signature:
            return echostr
        else:
            return ""

    elif request.method == 'POST':
        xmldata = request.args
        # print(xmldata)
        # xm1=et.
        # xml_rec = et.fromstring(xmldata)
        xml_rec = request.stream.read()
        # print(rec)
        # xml_rec = et.fromstring(rec)

        ToUserName = xml_rec.find('ToUserName').text
        fromUser = xml_rec.find('FromUserName').text
        MsgType = xml_rec.find('MsgType').text
        Content = xml_rec.find('Content').text
        MsgId = xml_rec.find('MsgId').text

        return ToUserName,Content

access_token='23_M17nil_Ym83RcvykuMSD4RvSdAaNHLyeeDeKaWPVrQ6AsZUZ0oqNKQwgFCyla-Fd1cpMBGVyib9BBtnMfwkg8JEA9N5usDzQxLatxzh9FFg_idNJZObaKXcysXWryOyPnv5VB-_knWmwhRngSUFbAEAACN'
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
ToUserName,Content=wechat()
sendmsg(ToUserName,Content)




app.run(port=80,debug=True,host='0.0.0.0')
if __name__ == '__main__':
    app.run()
