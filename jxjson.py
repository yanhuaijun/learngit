# coding: utf-8  json打开文档数据解析，保存到表格
import xlwt

#解析数据
def jxjosn():
    jx=[]
    f = open('C:/Users/qaunhou006/Desktop/test.txt', encoding='utf-8')   #文档路径，注意先把ture改为Turea，null改为"null"
    f = f.read()
    list1 = eval(f)
    for x,i in zip(range(1,150),list1['data']):
        list=x,i['mobileNo'],i['memberId'],i['userName']
        print(*list)   #加 * 号可以把打印列表外面的（）去掉
        jx.append(list)
    return jx
jx=jxjosn()
#把解析好的数据写入表格中
def write():
    workbook = xlwt.Workbook('d:\erp.xlsx')  #创建一个Excel文件
    worksheet = workbook.add_sheet('sheetname',cell_overwrite_ok = True)  #创建一个sheet
    print('开始写入表格。。。。')
    worksheet.write(0,0,"序号")
    worksheet.write(0,1,"手机号码")
    worksheet.write(0,2,"memberId")
    worksheet.write(0,3,"name")
    # worksheet.write(0,4,"发布时间")
    for i,x in zip(range(1,50),jx):
        worksheet.write(i,0,x[0])
        worksheet.write(i,1,x[1])
        worksheet.write(i,2,x[2])
        worksheet.write(i, 3, x[3])
        # worksheet.write(i, 4, x[0])
    workbook.save('d:\erp.xlsx')
    print('保存表格成功。。。。')

# jxjosn()
# write()