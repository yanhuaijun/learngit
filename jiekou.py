# import flask,json
# server=flask.Flask(__name__)#__name__代表当前的python文件。把当前的python文件当做一个服务启动
#
# @server.route('/index',methods=['get','post'])#第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get
# def index():
#     res={'msg':'这是我开发的第一个借口','msg_code':0}
#     return json.dumps(res,ensure_ascii=False)
#
# server.run(port=7777,debug=True,host='0.0.0.0')
# from flask_cors import CORS
import pymysql
import flask,json
server=flask.Flask(__name__)#__name__代表当前的python文件。把当前的python文件当做一个服务启动

# CORS(server, resources=r'/*')
@server.route('/index',methods=['get','post'])#第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get
def index():
    res={'msg':'这是我开发的第一个借口','msg_code':0}
    return json.dumps(res,ensure_ascii=False)

#阿里云数据库
def my_db(sq1):
    conn = pymysql.Connect(
        host='localhost',##mysql服务器地址
        port=3306,##mysql服务器端口号
        user='root',##用户名
        passwd='',##密码  J5p";~OVazNl%y)?
        db='mood_cabin',##数据库名
        charset='utf8',##连接编码
    )

    # cursor = con.cursor()  # 获取游标
    # sql = 'select * from my_user where username="%s";' % username
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sq1)
    uer = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return uer



#注册函数
@server.route('/reg',methods=['post'])#只有在函数前加上@server.route (),这个函数才是个接口，不是一般的函数
def reg():
    username=flask.request.values.get('username')
    passwd=flask.request.values.get('passwd')
    if username and passwd:
        sql='select * from mood_cabin_user where username="%s";'%username
        uer=my_db(sql)
        print(sql)
        if uer:
            res={'msg':'用户已存在','msg_code':2001}
        else:
            sql='INSERT INTO`my_user`(`username`, `passwd`, `is_admin`) VALUES("%s","%s",0);'%(username,passwd)
            my_db(sql)
            res={'msg':'恭喜你，注册成功！','msg_code':0}
    else:
        res={'msg':'参数错误，请输入正确！','msg_code':1001} #1001表示必填接口未填
    return json.dumps(res,ensure_ascii=False)
# server.run(port=7777,debug=True,host='0.0.0.0')
#端口不写默认是5000.debug=True表示改了代码后不用重启，会自动帮你重启.host写0.0.0.0，别人就可以通过ip访问接口。否则就是127.0.0.1


#http://127.0.0.1:7777/login?username=aa1234&passwd=123456
@server.route('/login',methods=['get'])#登录函数
def login():
    username=flask.request.values.get('username')
    pwd=flask.request.values.get('passwd')
    print('11')
    if username and pwd:
        sql='select * from mood_cabin_user where username="%s" and pwd="%s";'%(username,pwd)
        uer=my_db(sql)
        print(sql)
        if uer:
            res = {'msg': '欢迎你，登录成功！', 'msg_code': 2001}
        else:
            # sql='INSERT INTO`my_user`(`username`, `passwd`, `is_admin`) VALUES("%s","%s",0);'%(username,passwd)
            # my_db(sql)
            res={'msg':'用户名密码错误！','msg_code':10001}
    else:
        res={'msg':'参数错误，请联系管理员！','msg_code':1001} #1001表示必填接口未填
    return json.dumps(res,ensure_ascii=False)
server.run(port=8087,debug=True,host='0.0.0.0')