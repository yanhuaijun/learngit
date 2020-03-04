# coding: utf-8  从表格取数据放在URL里面循环
import requests
import xlrd
import time


##从表格取数据放在URL里面循环代码如下
# list=["safdsfasdfas","319hacsregp"]
# for i in list:
#     r=requests.get("http://192.168.1.201:15001/activity/activityDrawRoster/queryWinningInfo?acCode="+i)
#     print(r.json())

# workbook = xlrd.open_workbook('C:/Users/qaunhou006/Desktop/test.xlsx')  #表格路径
# table = workbook.sheets()[0]   #第一个表[0]

# print(table.nrows)
# print(table.ncols)
# print(table.row_values(0))
# print(table.col_values(0))
# print(table.cell(1,0).value)   #第一行、0列
# list=["safdsfasdfas","319hacsregp"]  http://192.168.1.201:15001

# for j in range(0,100):
#     i = table.cell(j, 0).value
#     r=requests.get("http://172.16.1.118:1114/activity/activityDrawRoster/queryWinningInfo?acCode="+i)
#     print(j)
#     print(r.json()["data"])
#     # print(r.json()["data"]["acCode"])
#     # if r.json()["data"]["data"] != None:
#     #
#     #   print(r.json()["data"]["acCode"])
#     time.sleep(0.2)

# -*- coding: UTF-8 -*-
# import xlsxwriter
import xlwt
import datetime
import time

#startTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
#print startTime
startTime1 = time.time()
#print startTime1

# workbook = xlwt.Workbook('d:\kami1.xlsx')  #创建一个Excel文件
# worksheet = workbook.add_sheet('sheetname',cell_overwrite_ok = True)            #创建一个sheet

workbook = xlrd.open_workbook('C:/Users/qaunhou006/Desktop/test.xlsx')  #表格路径
worksheet = workbook.sheets()[0]   #第一个表[0]

#title 写入Excel  行，列


worksheet.write(0,0,"名称1")
worksheet.write(0,1,"名称2")
worksheet.write(0,2,"名称3")
for i in range(1,6):
    li1='语文'+str(i)
    li2 = '数学' +str(i)
    li3 = 'English' + str(i)
    worksheet.write(i,0,li1)
    worksheet.write(i,1,li2)
    worksheet.write(i,2,li3)




# for i in range(1,100):
#     num0 = bytes(i+1)
#     num = bytes(i)
#     row = 'A' + num0
#     data = [u'学生'+num,num,]
#     worksheet.write_row(row, data)
#     i+=1

workbook.save('d:\kami1.xlsx')

#time.sleep(60)
#endTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#结束
#print endTime

endTime1 = time.time()
#print endTime1

print(endTime1-startTime1)
