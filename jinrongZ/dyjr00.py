from jinrongZ.huobigupiao import huobi,gp
import time
print ('当前为第：'+time.strftime('%U')+'周')
#CW当周 NW次周 CQ季度
dmlist=["BTC_CW","BTC_NW","XRP_CQ"]
bj=0.2997
list2=["btcusdt","ethusdt","bchusdt","eosusdt","xrpusdt","htusdt"]

#恒生电子 sh600570 #三花智控  sz002050   '01801017'
list1 = ["sh000001","sz000917","sh600705","sz000063","sh601066","sh600570","sh600150",'sz000951',
         "sz002475",'sz002090','sh600699','sh600518','sz002746',]

g1="sz002746"
cb1=17.139
je1=46000

g2="sz002475"
cb2=18.814
je2=0

i=3
if i==1:
    while True:
        gp.gupiao(list1,g1,cb1,je1,g2,cb2,je2)  #12 13 14 22 27 33 1 5 11
        time.sleep(4)                            #31 21 02 30 06 15 02

elif i==2:
    while True:
        huobi.usdt()
        huobi.hb(list2)
        time.sleep(3)

elif i==3:
    while True:
        huobi.hb(list2)
        time.sleep(3)
        gp.gupiao(list1, g1, cb1, je1, g2, cb2, je2)
        time.sleep(4)

else:
    huobi.usdt()
    huobi.hb(list2)
    gp.gupiao(list1,g1,cb1,je1,g2,cb2,je2)


