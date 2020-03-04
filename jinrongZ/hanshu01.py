import requests
from bs4 import BeautifulSoup

def gupiao(list1):
    # 股票价格
    print('')
    print("-------价格------")
    url2 = "http://qt.gtimg.cn/q="
    # list1 = ["sh000001", "sz000917", "sh600150", "sz300692", "sh600705", "sz000100", "sh600611", "sz002031", ]
    for i in list1:
        a = requests.get(url2 + i)
        # print(a.headers)
        # print(a.text)
        b = a.text
        c = b.split("~")
        # print(c)
        print(c[1], "换手率" + c[38] + "%", "市盈率" + c[39], "市值(" + c[45] + "亿--" + c[44] + "亿)",
              "成交额:" + "%.3f" % (float(c[37]) / 10000) + "亿元", " 当前价:" + c[3] + "￥", "涨幅" + c[32] + "%")
        # print(''"---------")
# list1 = ["sh000001", "sz000917", "sh600150", "sz300692", "sh600705", "sz000100", "sh600611", "sz002031", ]
# gupiao(list1)