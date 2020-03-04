#此代码用于MySQL数据库批量造数据
import pymysql
import random
import time
from datetime import datetime
# conn = pymysql.connect(user="用户名", password="密码", port="3306", db="数据库名", host="数据库主机地址", charset="utf8")  # 创建数据库连接
# conn = pymysql.connect("192.168.1.10","developer","13147",'J5p";~OVazNl%y)?',"caimei")

#1.连接数据库
con = pymysql.Connect(
    host='192.16800.1.10',##mysql服务器地址
    port=13147,##mysql服务器端口号
    user='developer',##用户名
    passwd='J5p";~OVazNl%y)?',##密码  J5p";~OVazNl%y)?
    db='caimei',##数据库名
    charset='utf8',##连接编码
)

cursor = con.cursor()  # 获取游标

# sq3="SELECT * FROM cm_coupon;"
# cursor.execute(sq3)
# #Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
# # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# # fetchall(): 接收全部的返回结果行.
# data = cursor.fetchone()
# data1= cursor.fetchall()
# print(data1)

#2.编写sql语句
sql1=''
sql2=''
sql3=''
sq5="INSERT INTO `caimei`.`cm_coupon` (`couponCode`, `couponAmount`, `discount`, `useStartDate`, `useEndDate`, `status`, `couponType`, `threshold`, `useDescription`, `createBy`, `createDate`, `updateBy`, `updateDate`, `delFlag`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for i in range(1, 101):   #循环100次，就是往数据库里面插入100条数据
    #下面设置变量
    list5 = [8888, 666, 999, 777, 1238, 55]
    couponAmount = str(random.choice(list5))  #优惠金额
    list6 =[0,1]
    couponType =str(random.choice(list6))    #优惠券类型
    #执行sql语句，以及要插入的数据
    cursor.execute(sq5,( 'CMYHJ00'+str(i),couponAmount, '0.8', '2018-10-09 12:55:12', '2018-11-10 12:55:12', '0', couponType, '华熙优惠券满多少使用等', '通用还是指定商品可用', '1', '2018-11-05 10:05:02', '1', '2018-11-05 10:05:02', '0'))
    cursor.execute(sql1,)
    cursor.execute(sql2, )
    cursor.execute(sql3, )

    con.commit()  # 提交事务
con.close()  #关闭










# sq2 = "INSERT INTO yy1 (mobile,name) VALUES (%s,%s)"
# sql = "INSERT INTO yy (createtime,updatatime,citizen_id,title,community_id,question_status,community_type) VALUES (%s,%s,%s,%s,%s,%s,%s)"  # sql语句
# for i in range(1, 5):
#     list = [130, 131, 132, 134, 136, 137, 138, 139]
#     num1=str(random.choice(list))
#     mobile = num1 + str("".join(random.choice("0123456789") for i in range(8)))
#
#     list1=["AAAA","DDDD","EEEE","GGGG","HHHH","KKKK"]
#     a = str(random.choice(list1))
#     a1 = random.randint(0, 123456789)
#     aa=a+str(a1)
#
#     create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     cursor.execute(sql, (
#     create_time, "2018-06-04 10:51:39",aa, "AAA添加的测试数据" + str(i),mobile, "1","4"))  # 传值
#
#     cursor.execute(sq2,(mobile,aa))
#     conn.commit()  # 提交事务
#
#
# time.sleep(3)
# cursor.execute(sq3)
# data2 = cursor.fetchall()
#
# print(data2)


