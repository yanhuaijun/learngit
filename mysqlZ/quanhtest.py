import pymysql
import random
import time
def qhmysql(sq2,sq3):
    con = pymysql.Connect(
        host='113.98.62.218',##mysql服务器地址  泉后测试库
        port=3306,##mysql服务器端口号
        user='devoa',##用户名
        passwd='devoa*111',##密码  J5p";~OVazNl%y)?
        db='queenoa',##数据库名
        charset='utf8',##连接编码
    )

    cursor = con.cursor()  # 获取游标

    # sq2="SELECT * FROM sys_account WHERE mobile_no =13066875865;"
    # cursor.execute(sq2)
    #
    # data = cursor.fetchone()
    # data1= cursor.fetchall()
    # print(data)

    # sq3="SELECT * FROM sys_account "
    cursor.execute(sq3)
    data1= cursor.fetchall()

    for i in range(0,100):
        print(data1[i])

    cursor.execute(sq2)

    data = cursor.fetchone()
    data1 = cursor.fetchall()
    print(data)
    # con.close()  #关闭



sq2="SELECT account_id,user_name,mobile_no,open_id,wechat_app_id FROM sys_account WHERE mobile_no =13066875865;"
sq3="SELECT * FROM sys_account"
qhmysql(sq2,sq3)