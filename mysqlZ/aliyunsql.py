import pymysql,requests
def my_db(msg):
    conn = pymysql.Connect(
        host='47.106.143.70',##mysql服务器地址
        port=3306,##mysql服务器端口号
        user='yhj666',##用户名
        passwd='aa123456',##密码  J5p";~OVazNl%y)?
        db='yhj666',##数据库名
        charset='utf8',##连接编码
    )
    sq1 = 'SELECT * FROM cityid WHERE city_name LIKE "%s"' %('%'+msg+'%')
    # cursor = con.cursor()  # 获取游标
    # sql = 'select * from my_user where username="%s";' % username
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sq1)
    uer = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return uer
    #data1 = cursor.fetchall()
    # print(data1[0][1])
    # uer=data1[0][1]

# sq1='select * from my_user where username="a12121"'
# print(my_db(sq1))



#输入你要查询天气的城市
msg='岳阳'
# print(my_db(msg))
print(my_db(msg)['city_code'])

def tqyb():
    url1="http://t.weather.sojson.com/api/weather/city/"+my_db(msg)['city_code']
    url2 = "http://t.weather.sojson.com/api/weather/city/101280601"

    re=requests.get(url1)
    # print(re.json()["cityInfo"])forecast #0102番禺 0101广州市 深圳市0601 白云0110  天河0109
    # print(re.json()["cityInfo"])
    # print(re.json()["data"]["forecast"][0])

    tq0=re.json()["cityInfo"]
    tq=re.json()["data"]["forecast"][0]
    tq1=re.json()["data"]
    # print("当前城市:"+tq0["parent"],tq0["city"])
    tq00="当前城市:"+tq0["parent"],tq0["city"],"今天"+tq["week"],"最"+tq["high"],"最"+tq["low"]\
        ,"天气类型:"+tq["type"],tq["fx"],tq["fl"],"温馨提示："+tq["notice"]\
        ,"湿度:"+tq1["shidu"],"空气质量:"+tq1["quality"],"感冒指数:"+tq1["ganmao"],"天气更新时间:"+tq0["updateTime"]
    print(tq00)

# tqyb()





def my_db1(insert_sql):
    con = pymysql.Connect(
        host='47.106.143.70',##mysql服务器地址
        port=3306,##mysql服务器端口号
        user='yhj666',##用户名
        passwd='aa123456',##密码  J5p";~OVazNl%y)?
        db='yhj666',##数据库名
        charset='utf8',##连接编码
    )

    cursor = con.cursor()  # 获取游标
    # sql = 'select * from my_user where username="%s";' % username

    cursor.execute(insert_sql)
    data1 = cursor.fetchall()