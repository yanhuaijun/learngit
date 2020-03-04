import requests

#
# urlist=["XRP_CW","XRP_NW","XRP_CQ"]
# url="https://api.hbdm.com/market/history/kline?symbol="
# ur2="&period=1day&size=2"
# for i in urlist:
#     r1=requests.get(url+i+ur2)
#     # print(r1.json())
#     re=r1.json()["data"][1]
#     # print(re)
#     # print("当前价:"+str(re["close"]))
#     #涨幅计算(re["close"]-re["open"])/re["open"]
#     zh="%.2f%%"%(((re["close"]-re["open"])/re["open"])*100)
#     # print("涨幅:"+zh)
#     # print(i,"当前价:"+str(re["close"]),"涨幅:"+str(zh))
#     # 收益计算
#     bj = 0.2997
#     sy = "%.2f%%" % (((re["close"] - bj) / bj) * 100)
#     # print("收益:"+sy)
#     pr1=i,"当前价:"+str(re["close"]),"涨幅:"+str(zh)
#     pr2=i,"当前价:"+str(re["close"]),"涨幅:"+str(zh),"收益:"+sy
#     if i=="XRP_CQ":
#         print(i,"当前价:"+str(re["close"]),"涨幅:"+str(zh),"收益:"+sy)
#     else:
#         print(i,"当前价:"+str(re["close"]),"涨幅:"+str(zh))
class dm:

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


dmlist=["BTC_CW","BTC_NW","XRP_CQ"]
bj=0.2997
dm.hbdm(dmlist,bj)