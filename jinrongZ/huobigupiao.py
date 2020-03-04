import requests,time
from bs4 import BeautifulSoup


#比特币usdt
url0="https://otc-api.eiijo.cn/v1/data/trade-market?country=37&currency=1&payMethod=0&currPage=1&coinId=1&tradeType=sell&blockType=general&online=1"

#USDT
url1="https://otc-api.eiijo.cn/v1/data/trade-market?country=37&currency=1&payMethod=0&currPage=1&coinId=2&tradeType=sell&blockType=general&online=1"

#以太坊usdt
url2="https://otc-api.eiijo.cn/v1/data/trade-market?country=37&currency=1&payMethod=0&currPage=1&coinId=3&tradeType=sell&blockType=general&online=1"

#EOSusdt
url3="https://otc-api.eiijo.cn/v1/data/trade-market?country=37&currency=1&payMethod=0&currPage=1&coinId=5&tradeType=sell&blockType=general&online=1"

#火腿usdt
url4="https://otc-api.eiijo.cn/v1/data/trade-market?country=37&currency=1&payMethod=0&currPage=1&coinId=4&tradeType=sell&blockType=general&online=1"

#火币官网接口
url5="https://www.huobi.co/-/x/pro/market/overview5?r=wrka1"

class huobi:
    def usdt():
        #USDT价格
        url1="https://otc-api.eiijo.cn/v1/data/trade-market?country=37&currency=1&payMethod=0&currPage=1&coinId=2&tradeType=sell&blockType=general&online=1"
        a = requests.get(url1)
        # print(a.headers)
        b= a.json()["data"]
        # print (str(b[0]["payName"][14:18]))
        print("-------USDT价格------")
        for i in range(0,10):
            print("USDT:"+str(b[i]["payName"][14:18]) ," 价格:"+str(b[i]["price"])," 限额:"+str(b[i]["minTradeLimit"])+"元-",str(b[i]["maxTradeLimit"])+"元"," 用户:"+str(b[i]["userName"]))

    def hb(list2):
        print('')
        print("-------^-^-----")
        url88="https://api.huobi.pro/market/history/kline?period=1day&size=200&symbol=btcusdt"
        url881="https://www.huobi.co/-/x/pro/market/detail/merged?symbol=eosusdt"
        url883="https://www.huobi.co/-/x/pro/market/detail/merged?symbol="
        url882="https://www.huobi.io/-/x/pro/market/history/kline?period=1day&size=1&symbol="
        # list2=["btcusdt","ethusdt","eosusdt","bchusdt","xrpusdt","htusdt","ltcusdt"]
        for i in list2:
            a = requests.get(url882+i)
            b= a.json()
            # print(b)
            # print(b["data"][0]["close"])
            # 涨幅计算
            w=str("%.2f%%"%(((b["data"][0]["close"]-b["data"][0]["open"])/b["data"][0]["open"])*100))
            print(i,"现价"+str(b["data"][0]["close"])+" US","涨幅："+w)

    #火币合约
    def hbdm(dmlist,bj):
        print('')
        # dmlist = ["XRP_CW", "XRP_NW", "XRP_CQ"]
        url = "https://api.hbdm.com/market/history/kline?symbol="
        ur2 = "&period=1day&size=2"
        for i in dmlist:
            r1 = requests.get(url + i + ur2)
            # print(r1.json())
            re = r1.json()["data"][1]
            # print(re)
            # print("当前价:"+str(re["close"]))
            # 涨幅计算(re["close"]-re["open"])/re["open"]
            zh = "%.2f%%" % (((re["close"] - re["open"]) / re["open"]) * 100)
            # print("涨幅:"+zh)
            # print(i,"当前价:"+str(re["close"]),"涨幅:"+str(zh))
            # 收益计算
            # bj = 0.2997
            sy = "%.2f%%" % (((re["close"] - bj) / bj) * 100)
            # print("收益:"+sy)
            pr1 = i, "当前价:" + str(re["close"]), "涨幅:" + str(zh)
            pr2 = i, "当前价:" + str(re["close"]), "涨幅:" + str(zh), "收益:" + sy
            if i == "XRP_CQ":
                print(i, "当前价:" + str(re["close"]), "涨幅:" + str(zh), "收获:" + sy)
            else:
                print(i, "当前价:" + str(re["close"]), "涨幅:" + str(zh))


#股票价格
class gp:
    def gupiao(list1,g1,cb1,je1,g2,cb2,je2):
        print('')
        print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("-------价格------")
        url2="http://qt.gtimg.cn/q="
        # list1=["sh000001","sz000917","sh600150","sz300692","sh600705","sz000100","sh600611","sz002031",]
        for i in list1:
            time.sleep(0.2)
            a = requests.get(url2+i)
            # print(a.headers)
            # print(a.text)
            b=a.text
            c=b.split("~")
            # print(c)
            # print(i, c[1], "换手率" + c[38] + "%", "市盈率" + c[39], "市值(" + c[45] + "亿--" + c[44] + "亿)",
            #       "成交额:" + "%.3f" % (float(c[37]) / 10000) + "亿元", " 当前价:" + c[3] + "￥", "涨幅" + c[32] + "%")
            # print(''"---------")
            # cb1=64.056    #恒生电子 sh600570
            # cb2=11.164    #三花智控  sz002050
            if i == g1:
                c1=float(c[3])
                syl = "%.2f%%" % (((c1 - cb1) / cb1) * 100)
                sy = '%.0f'%(((c1 - cb1) / cb1)*je1)
                # print(sy)
                print(i, c[1], "换手率" + c[38] + "%", "市盈率" + c[39], "市值(" + c[45] + "亿--" + c[44] + "亿)",
                      "成交额:" + "%.3f" % (float(c[37]) / 10000) + "亿元", " 当前价:" + c[3] + "￥", "涨幅" + c[32] + "%", "  "+syl," "+str(sy))
            elif i== g2:
                c1 = float(c[3])
                sy2 = "%.2f%%" % (((c1 - cb2) / cb2) * 100)
                sy = '%.0f' % (((c1 - cb1) / cb1) * je2)
                # print(sy)
                print(i, c[1], "换手率" + c[38] + "%", "市盈率" + c[39], "市值(" + c[45] + "亿--" + c[44] + "亿)",
                      "成交额:" + "%.3f" % (float(c[37]) / 10000) + "亿元", " 当前价:" + c[3] + "￥", "涨幅" + c[32] + "%","  " +sy2," "+str(sy))
            else:
                print(i, c[1], "换手率" + c[38] + "%", "市盈率" + c[39], "市值(" + c[45] + "亿--" + c[44] + "亿)",
                      "成交额:" + "%.3f" % (float(c[37]) / 10000) + "亿元", " 当前价:" + c[3] + "￥", "涨幅" + c[32] + "%")

# usdt()
# huobi()
# gupiao()



# #火币首页价格
# a = requests.get(url5)
# b= a.json()["data"]
# print(b[4]["symbol"])
# print(b[1])
# print(b[2])
# print(b[3])
# print((str(b[1]["close"]-b[1]["open"])/b[1]["open"]*100),+str("%"))
#
# # #比特币价格
# # a = requests.get(url0)
# # b= a.json()["data"]
# # print("-------比特币价格------")
# # for i in range(0,5):
# #      print("BTC:"+str(b[i]["payName"][14:18]) ," 价格:"+str(b[i]["price"])," 限额:"+str(b[i]["minTradeLimit"])+"元-",str(b[i]["maxTradeLimit"])+"元")
# #
# # #以太坊
# # a = requests.get(url2)
# # b= a.json()["data"]
# # print("-------以太坊价格------")
# # for i in range(0,5):
# #      print("ETH:"+str(b[i]["payName"][14:18]) ," 价格:"+str(b[i]["price"])," 限额:"+str(b[i]["minTradeLimit"])+"元-",str(b[i]["maxTradeLimit"])+"元")
# #
# # #EOS
# # a = requests.get(url3)
# # b= a.json()["data"]
# # print("-------EOS价格------")
# # for i in range(0,5):
# #      print("EOS:"+str(b[i]["payName"][14:18]) ," 价格:"+str(b[i]["price"])," 限额:"+str(b[i]["minTradeLimit"])+"元-",str(b[i]["maxTradeLimit"])+"元")
# #
# # #火腿
# # a = requests.get(url4)
# # b= a.json()["data"]
# # print("-------火腿价格------")
# # for i in range(0,5):
# #      print("HT:"+str(b[i]["payName"][14:18]) ," 价格:"+str(b[i]["price"])," 限额:"+str(b[i]["minTradeLimit"])+"元-",str(b[i]["maxTradeLimit"])+"元")
#
#
#
#
#
#
#
#
#
#
#
#
#
# # a.encoding=a.apparent_encoding
# # # print(a.text)
# # soup = BeautifulSoup(a.text,features='html.parser')
#
#
#
# # aa1=soup.pre
# # aa2=soup.find_all("tr")
# # # print(aa1)
# # print(aa1)
# # aa2=soup.find_all("ul")
# # print(aa2[2])
#
# # a1=soup.find_all("h2")  symbol_list
# # print("电影名称："+a1[0].text)
# # aa = soup.find(class_='play-list').text
# # # print(aa)
# # if   u"高清" in aa :
# #     print(a1[0].text+"可以观看")
# # else:
# #     print(a1[0].text+"：不是高清电影不建议观看")
# #
# # key1=x
# # key2=y
# #
# # key1=x
# # key2=y
# # sum=x+y
# # print(sum)



# #快递100 接口
# url100="http://www.kuaidi100.com/query?type=tiantian&postid=669696824735&temp=0.13331742100283583&phone="
# a = requests.get(url100)
# b= a.json()
# print(b["data"][0]["context"])
# print(b["data"][1]["context"])
# print(b["data"][2]["context"])
# print(b["data"][3]["context"])
# print(b["data"][4]["context"])
# print(b["data"][5]["context"])
# print(b["data"][6]["context"])
# print(b["data"][7]["context"])
# print(b["data"][8]["context"])
# print(b["data"][9]["context"])

