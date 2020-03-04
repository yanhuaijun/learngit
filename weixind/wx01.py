# -*- coding: utf-8 -*-


from datetime import datetime, timedelta
from flask import Flask, jsonify, request, url_for
# from weixin import Weixin, WeixinError
import weixin


app = Flask(__name__)
app.debug = True


# 具体导入配
# 根据需求导入仅供参考
app.config.fromobject(dict(WEIXIN_APP_ID='wx87d17a791d346b6b', WEIXIN_APP_SECRET='8d2d3270d9c8c564056dbe43110a7dce'))
# 初始化微信
# weixin = Weixin()
# weixin.init_app(app)
# # 或者
# weixin = Weixin(app)

app.add_url_rule("/", view_func=weixin.view_func)
@weixin.all
def all(**kwargs):
        """
        监听所有没有更特殊的事件
        """
        return weixin.reply(kwargs['sender'], sender=kwargs['receiver'], content='all')


@weixin.text()
def hello(**kwargs):
        """
        监听所有文本消息
        """
        return "hello too"


@weixin.text("help")
def world(**kwargs):
        """
        监听help消息
        """
        return dict(content="hello world!")


@weixin.subscribe
def subscribe(**kwargs):
        """
        监听订阅消息
        """
        print (kwargs)
        return "欢迎订阅我们的公众号"