# coding: utf-8 爬取微博热搜榜
import requests,time
from bs4 import BeautifulSoup
import lxml

ur1='https://s.weibo.com/top/summary?cate=realtimehot'
ur2=''

r1=requests.get(ur1)
print(r1)
# print(r1.text)
print ('当前时间：'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
bs = BeautifulSoup(r1.text,'lxml')
for i in range(1,50):
    # print('#pl_top_realtimehot > table > tbody > tr:nth-child('+str(i)+')> td.td-02 > a')
    he='#pl_top_realtimehot > table > tbody > tr:nth-child('+str(i)+')'

    p1=bs.select( he+'> td.td-02 > a')
    p2=bs.select(he+' > td.td-02 >span')
    if i == 1:
        print(i-1,p1[0].string)
    else:
        print(i-1,p1[0].string,p2[0].string)

#代码演示
# p1=bs.select( '#pl_top_realtimehot > table > tbody > tr:nth-child(2)> td.td-02 > a')
# print('打印a标签全部: '+str(p1[0]))
# print('打印a标签的标签: '+str(p1[0].attrs))
# print('打印a标签的链接: '+str(p1[0].attrs['href']))
# print('打印a标签的文字: '+str(p1[0].string))
