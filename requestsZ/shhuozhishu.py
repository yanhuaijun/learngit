# coding: utf-8 此代码用于查询生活指数
import requests
import json

def shzs():
    #广州生活指数
    ur1="http://d1.weather.com.cn/zs_index/101280101.html?_=1561449792583"
    # re=requests.get(ur1)

    headers = {'Accept':'*/*',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
               'Host': 'd1.weather.com.cn',
                'Referer':'http://www.weather.com.cn/life/',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400',
               }
    r = requests.get(ur1,headers=headers,verify=False)
    r.encoding='utf-8'
    # print(r.text)
    # print(type(r.text))
    jd = json.loads(r.text.strip('var dataZS='))    #移除改var data=将其变为json数据
    # print(jd)
    zs=jd['zs']
    ssd=zs['co_name']+':'  #舒适度
    cy=zs['ct_name']+':'  #穿衣
    fs=zs['fs_name']+':'  #防晒
    gm=zs['gm_name']+':'  #感冒
    ls=zs['ls_name']+':'  #晾晒指数
    xq=zs['xq_name']+':'  #心情
    ys=zs['ys_name']+':'  #雨伞
    zs1=zs['zs_name']+':'  #中暑
    gzzs = jd['cn'], zs1, zs['zs_des_s'], fs, zs['fs_hint'], ls, zs['ls_des_s'], cy, zs['ct_hint'], \
           zs['ct_des_s'], gm, zs['gm_des_s'], ssd, zs['co_des_s'], ys, zs['ys_hint'], zs['ys_des_s']

    #深圳生活指数
    ur2='http://d1.weather.com.cn/zs_index/101280601.html?_=1561527678118'

    # headers = {'Accept': '*/*',
    #            'Accept-Encoding': 'gzip, deflate',
    #            'Accept-Language': 'zh-CN,zh;q=0.9',
    #            'Connection': 'keep-alive',
    #            'Host': 'd1.weather.com.cn',
    #            'Referer': 'http://www.weather.com.cn/weather1d/101280601.shtml',
    #            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400',
    #            }
    r2 = requests.get(ur2,headers=headers,verify=False)
    r2.encoding='utf-8'
    # print(r2.text)
    # print(type(r2.text))

    jd1 =json.loads(r2.text.strip('var dataZS='))
    # print(jd1)

    zs=jd1['zs']
    ssd=zs['co_name']+':'  #舒适度
    cy=zs['ct_name']+':'  #穿衣
    fs=zs['fs_name']+':'  #防晒
    gm=zs['gm_name']+':'  #感冒
    ls=zs['ls_name']+':'  #晾晒指数
    xq=zs['xq_name']+':'  #心情
    ys=zs['ys_name']+':'  #雨伞
    zs1=zs['zs_name']+':'  #中暑

    szzs=jd1['cn'],zs1,zs['zs_des_s'],fs,zs['fs_hint'],ls,zs['ls_des_s'],cy,zs['ct_hint'],\
         zs['ct_des_s'],gm,zs['gm_des_s'],ssd,zs['co_des_s'],ys,zs['ys_hint'],zs['ys_des_s']

    return szzs,gzzs
szzs,gzzs=shzs()
print(gzzs)
print(szzs)