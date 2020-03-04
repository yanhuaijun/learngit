# coding: utf-8 ##泉后掌柜销售素材与培训接口从表格获取URL参数
import requests,json,time
from bs4 import BeautifulSoup
import xlrd
def open(url,openID):
    workbook = xlrd.open_workbook('C:/Users/qaunhou006/Desktop/jiekou.xlsx')  #表格路径
    table = workbook.sheets()[0]   #第一个表[0]
    print(table.nrows)  #打印总共有多少行
    print(table.ncols)  #打印总共有多少列
    # print(table.row_values(0))  #打印第一行
    # print(table.col_values(0))  #打印第一列
    # print(table.cell(1,0).value)   #第一行、0列
    # print(table.cell(1,1).value)
    print('---------泉后掌柜------------')
    for jj in range(1,table.nrows):
        a = table.cell(jj, 0).value  ##接口名称
        b = table.cell(jj, 1).value  ##域名
        c = table.cell(jj, 2).value  ## 接口地址
        d = table.cell(jj, 3).value  ##接口参数
        e = table.cell(jj, 4).value
        f = table.cell(jj, 5).value
        g = table.cell(jj, 6).value
        h = table.cell(jj, 7).value
        i = table.cell(jj, 8).value
        j = table.cell(jj, 9).value
        data={d:openID,f:g,h:i}
        # print('--测试--'+j+'----')
        re=requests.get(url+c,params=data)  #如果表格直接传{a:b,c:d}参数，应该转换 params=eval({a:b,c:d})
        if re.status_code==200:
            # print(type(relogin.json()))
            re=(re.json())
            # print(re)  ##检查字段的时候要转换为str
            if j in str(re):
                print(a+'\033[1;32;0m--测试通过\033[0m')
            else:
                print(a + '\033[1;31;0m--不通过\033[0m')
                print(re)
            time.sleep(1)
        else:
            print(a+'\033[1;31;0m 报错：\033[0m'+str(re.status_code))    #打印报错接口以及响应码

def open1():
    workbook = xlrd.open_workbook('C:/Users/qaunhou006/Desktop/jiekou.xlsx')  #表格路径
    table = workbook.sheets()[1]   #第一个表[0]
    print(table.nrows)  #打印总共有多少行
    print(table.ncols)  #打印总共有多少列
    # print(table.row_values(0))  #打印第一行
    # print(table.col_values(0))  #打印第一列
    # print(table.cell(1,0).value)   #第一行、0列
    # print(table.cell(1,1).value)
    print('--------ERPAPP-------------')
    for jj in range(1,table.nrows):
        a = table.cell(jj, 0).value  ##接口名称
        b = table.cell(jj, 1).value  ##域名
        c = table.cell(jj, 2).value  ## 接口地址
        d = table.cell(jj, 3).value  ##接口参数
        e = table.cell(jj, 4).value
        f = table.cell(jj, 5).value
        g = table.cell(jj, 6).value
        h = table.cell(jj, 7).value
        i = table.cell(jj, 8).value
        j = table.cell(jj, 9).value
        data={d:e,f:g,h:i}
        # print('--测试--'+j+'----')
        re=requests.get(b+c,params=data)  #如果表格直接传{a:b,c:d}参数，应该转换 params=eval({a:b,c:d})
        if re.status_code==200:
            # print(type(relogin.json()))
            re=(re.json())
            # print(re)  ##检查字段的时候要转换为str
            if j in str(re):
                print(a+'\033[1;32;0m--测试通过\033[0m')
            else:
                print(a + '\033[1;31;0m--不通过\033[0m')
                print(re)
            time.sleep(1)
        else:
            print(a+'\033[1;31;0m 报错：\033[0m'+str(re.status_code))
url='https://wx4e4f7b3ce72d4d42.ttwx.quanhoo.com'
openID='38b108ec9d0dd33e50647a0988e95f58'
open(url,openID)

open1()