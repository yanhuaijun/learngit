# coding: utf-8 ##泉后掌柜销售素材与培训接口
import requests,json,time
from bs4 import BeautifulSoup

token='XTfc207029c163b0ecf143dc3d1d49b0f6'
keyword=''
data={'token':token,'keyword':keyword}
UR='http://wx4e4f7b3ce72d4d42.ttwx.quanhoo.com/erpapp/Distribution/getList.html'
re=requests.post(UR,params=data)
print(re.json())

token='XTfc207029c163b0ecf143dc3d1d49b0f6'
keyword=''
data={'token':token,'keyword':keyword}
UR='http://wx4e4f7b3ce72d4d42.ttwx.quanhoo.com/erpapp/Distribution/getTotal.html'
re=requests.post(UR,params=data)
print(re.json())

token='XTfc207029c163b0ecf143dc3d1d49b0f6'
keyword='群'
data={'keyword':keyword,'token':token}
UR='http://wx4e4f7b3ce72d4d42.ttwx.quanhoo.com/erpapp/Distribution/getList.html'
re=requests.post(UR,params=data)
print(re.json())

token='XTfc207029c163b0ecf143dc3d1d49b0f6'
keyword='40'
data={'jq_training_curriculum_id':keyword,'token':token}
UR='http://wx4e4f7b3ce72d4d42.ttwx.quanhoo.com/erpapp/Distribution/getDetail.html'
re=requests.post(UR,params=data)
print(re.json())



ur="https://wx4e4f7b3ce72d4d42.ttwx.quanhoo.com"
data={"openId":"38b108ec9d0dd33e50647a0988e95f58"}
login="/jiquanapi/login/index.html"
##销售素材最新接口
sucaizuixin="/jiquanapi/Discovery/index.html"
##销售素材最热接口
sucaizuire='/jiquanapi/Discovery/index.html'
zuiredata={'openId':'38b108ec9d0dd33e50647a0988e95f58','status':'2'}
##销售素材点赞接口
sucaidianzan='/jiquanapi/Discovery/getBannerList.html'
##销售素材我的消息接口
sucaixiaoxi='/jiquanapi/Discovery/getMessageList.html'
##培训个人信息接口
pxgrenxxi='/jiquanapi/curriculum_api/getUserLevel.html'
##培训上一次学习课程接口
pxsycxxi='/jiquanapi/curriculum_api/getUserLastCurriculum.html'
##培训课程分类接口
pxkcflei='/jiquanapi/curriculum_api/curriculumCategory.html'
##培训全部课程接口
pxqbkc='/jiquanapi/curriculum_api/index.html'
##培训学习任务接口
pxxxreu='/jiquanapi/curriculum_api/curriculumTask.html'
##培训学习历史记录接口
pxxxlsjlu='/jiquanapi/curriculum_api/history.html'
##培训课件搜索接口
pxss='/jiquanapi/curriculum_api/searchList.html'
ssdata={'openId':'38b108ec9d0dd33e50647a0988e95f58','keyword':'泉后'}
##培训日榜排行
pxrbph='/jiquanapi/mylevel/ranking.html'
##培训周榜排行
pxzbphdata={'openId':'38b108ec9d0dd33e50647a0988e95f58','type':2}

# print('登陆接口')
# relogin=requests.get(ur+login,params=data)
# print(relogin)
# print(relogin.text)
# login=eval(relogin.text)   ## str 转 字典
# print(login['msg'])
# ##销售素材最新接口
# print('销售素材最新接口')
# sucai01=requests.get(ur+sucaizuixin,params=data)
# print(sucai01.text)
# sucai01=eval(sucai01.text)
# print(sucai01['status'])
# ##销售素材最热
# print('销售素材最热接口')
# sucai02=requests.get(ur+sucaizuire,params=zuiredata)
# print(sucai02.json()['status'])
# print(sucai02.json())
#
# ##销售素材点赞接口
# print('销售素材点赞接口')
# sucai02=requests.get(ur+sucaidianzan,params=data)
# print(sucai02.json()['status'])
#
# ##销售素材我的消息接口
# print('销售素材我的消息接口')
# sucai02=requests.get(ur+sucaixiaoxi,params=data)
# print(sucai02.json()['status'])
#
# ##培训个人信息接口
# print('培训个人信息接口')
# sucai02=requests.get(ur+pxgrenxxi,params=data)
# print(sucai02.json()['status'])
#
# ##培训上一次学习课程接口
# print('培训上一次学习课程接口')
# sucai02=requests.get(ur+pxsycxxi,params=data)
# print(sucai02.json()['status'])
#
# ##培训课程分类接口
# print('培训课程分类接口')
# sucai02=requests.get(ur+pxkcflei,params=data)
# print(sucai02.json()['status'])
#
# ##培训全部课程接口
# print('培训全部课程接口')
# sucai02=requests.get(ur+pxqbkc,params=data)
# print(sucai02.json())
#
# ##培训学习任务接口
# print('培训学习任务接口 ')
# sucai02=requests.get(ur+pxxxreu,params=data)
# print(sucai02.json()['status'])
#
# ##培训学习历史记录接口
# print('培训学习历史记录接口 ')
# sucai02=requests.get(ur+pxxxlsjlu,params=data)
# print(sucai02.json()['status'])
#
# ##培训课件搜索接口
# print('培训课件搜索接口 ')
# sucai02=requests.get(ur+pxss,params=ssdata)
# print(sucai02.json()['status'])
#
# ##培训日榜排行
# print('培训日榜排行 ')
# sucai02=requests.get(ur+pxrbph,params=data)
# print(sucai02.json()['status'])
#
# ##培训周榜排行
# print('培训周榜排行 ')
# sucai02=requests.get(ur+pxrbph,params=pxzbphdata)
# print(sucai02.json()['status'])