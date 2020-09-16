# coding: utf-8 新闻汇总

import requests


def baidu():
    ur1='https://www.anyknew.com/api/v1/sites/baidu'
    r1=requests.get(ur1)
    # print(r1.json())
    # baidulist={'status': 0, 'msg': 'success', 'data': {'site': {'site': 'baidu', 'attrs': {'cn': '百度', 'logo': 'https://f0cdn.anyknew.com/static/logo/baidu_crop.png', 'url': 'https://www.baidu.com', 'iter': 68413}, 'subs': [{'items': [{'iid': 6855521, 'title': '张文宏等80名医生获中国医师奖', 'more': '488万', 'add_date': 1597812285, 'new_tag': True}, {'iid': 6855475, 'title': '拜登正式被提名为美国总统候选人', 'more': '471万', 'add_date': 1597810354, 'new_tag': True}, {'iid': 6855616, 'title': '牛奶咖啡斥何洛洛新歌抄袭', 'more': '438万', 'add_date': 1597816007, 'new_tag': True}, {'iid': 6855142, 'title': '河南未婚女子5地被结婚', 'more': '423万', 'add_date': 1597802575, 'new_tag': True}, {'iid': 6855186, 'title': '中国医师节 点亮医生愿望', 'more': '408万', 'add_date': 1597803486, 'new_tag': True}, {'iid': 6854792, 'title': '演员谢园去世', 'more': '394万', 'add_date': 1597794339, 'new_tag': False}, {'iid': 6855520, 'title': '李楠出任江苏男篮主教练', 'more': '380万', 'add_date': 1597812285, 'new_tag': True}, {'iid': 6855223, 'title': '特朗普反击奥巴马夫人', 'more': '354万', 'add_date': 1597804472, 'new_tag': True}, {'iid': 6854825, 'title': '马里发生军人哗变 总统总理被扣', 'more': '342万', 'add_date': 1597795643, 'new_tag': False}, {'iid': 6855615, 'title': '刘欣揭孟晚舟案背后隐情', 'more': '318万', 'add_date': 1597816007, 'new_tag': True}, {'iid': 6854824, 'title': '四川一男子江边拍洪水被卷走', 'more': '307万', 'add_date': 1597795643, 'new_tag': False}, {'iid': 6855396, 'title': '新冠病毒潜伏期即有传染性', 'more': '296万', 'add_date': 1597808520, 'new_tag': True}, {'iid': 6855395, 'title': '武汉车主已提车报道为假新闻', 'more': '286万', 'add_date': 1597808520, 'new_tag': True}, {'iid': 6855472, 'title': '洪水漫上重庆主城', 'more': '276万', 'add_date': 1597810354, 'new_tag': True}, {'iid': 6855614, 'title': '海天味业市值超越中石化', 'more': '266万', 'add_date': 1597816007, 'new_tag': True}, {'iid': 6855473, 'title': '纽约州长批评美政府抗疫不力', 'more': '257万', 'add_date': 1597810354, 'new_tag': True}, {'iid': 6855474, 'title': '台风海高斯减弱为强热带风暴', 'more': '248万', 'add_date': 1597810354, 'new_tag': True}, {'iid': 6854904, 'title': '王俊凯单曲封面设计师否认抄袭', 'more': '239万', 'add_date': 1597797594, 'new_tag': False}, {'iid': 6855497, 'title': '水旱灾害防御应急响应提升至Ⅱ级', 'more': '231万', 'add_date': 1597811240, 'new_tag': True}, {'iid': 6854182, 'title': '华为称会继续提供系统更新', 'more': '223万', 'add_date': 1597754096, 'new_tag': False}, {'iid': 6854203, 'title': '贪玩公司申请渣渣辉商标被驳回', 'more': '215万', 'add_date': 1597754944, 'new_tag': False}, {'iid': 6854231, 'title': '官方通报老人被狗绳绊倒后身亡', 'more': '207万', 'add_date': 1597755805, 'new_tag': False}, {'iid': 6854336, 'title': '村民被洪水围困屋顶挥旗求救', 'more': '200万', 'add_date': 1597759493, 'new_tag': False}, {'iid': 6854384, 'title': '秦皇岛现海市蜃楼景观', 'more': '193万', 'add_date': 1597761203, 'new_tag': False}, {'iid': 6854337, 'title': '约90名中国工人在以色列感染新冠', 'more': '186万', 'add_date': 1597759493, 'new_tag': False}, {'iid': 6854358, 'title': '特朗普宣布赦免美国女权运动领袖', 'more': '180万', 'add_date': 1597760394, 'new_tag': False}, {'iid': 6854795, 'title': '四川宜宾通报路面塌陷', 'more': '173万', 'add_date': 1597794339, 'new_tag': False}], 'attrs': {'cn': '热点', 'display': 10}}, {'items': [{'iid': 6855327, 'title': '未婚女子5地被结婚', 'more': '180.1万', 'add_date': 1597807414, 'new_tag': False}, {'iid': 6853979, 'title': '情缘和师徒不可兼得？', 'more': '153.8万', 'add_date': 1597747951, 'new_tag': False}, {'iid': 6854968, 'title': '谢园去世', 'more': '114.8万', 'add_date': 1597799043, 'new_tag': False}, {'iid': 6855248, 'title': '特朗普反击奥巴马夫人', 'more': '85.2万', 'add_date': 1597805282, 'new_tag': False}, {'iid': 6853642, 'title': '老人被狗绳绊倒后身亡', 'more': '66.6万', 'add_date': 1597739683, 'new_tag': False}, {'iid': 6853404, 'title': 'TES外卖事件已报案', 'more': '50.3万', 'add_date': 1597733330, 'new_tag': False}, {'iid': 6855247, 'title': '王鹤棣恋情', 'more': '44.6万', 'add_date': 1597805282, 'new_tag': False}, {'iid': 6855326, 'title': '湖南卫视晚会女艺人运镜', 'more': '43.4万', 'add_date': 1597807414, 'new_tag': False}, {'iid': 6855325, 'title': '秦皇岛海边出现海市蜃楼', 'more': '36.6万', 'add_date': 1597807414, 'new_tag': False}, {'iid': 6855425, 'title': '李子柒柳州建螺蛳粉厂', 'more': '35.5万', 'add_date': 1597809247, 'new_tag': False}, {'iid': 6855424, 'title': '马里军人哗变', 'more': '30.1万', 'add_date': 1597809247, 'new_tag': False}, {'iid': 6854967, 'title': '四川一男子拍洪水被卷走', 'more': '27.4万', 'add_date': 1597799043, 'new_tag': False}, {'iid': 6855423, 'title': '中国男子在东京遭绑架', 'more': '24.2万', 'add_date': 1597809247, 'new_tag': False}, {'iid': 6855422, 'title': '2020年中国医师节', 'more': '23.8万', 'add_date': 1597809247, 'new_tag': False}, {'iid': 6853742, 'title': '液化气罐跨省漂流到四川', 'more': '22.4万', 'add_date': 1597741655, 'new_tag': False}, {'iid': 6853056, 'title': 'NBA季后赛', 'more': '19.7万', 'add_date': 1597723348, 'new_tag': False}, {'iid': 6852972, 'title': '六旬男子加害百岁阿姨', 'more': '19.5万', 'add_date': 1597721451, 'new_tag': False}, {'iid': 6852624, 'title': '仝卓被写入公职人员学习读本', 'more': '19.5万', 'add_date': 1597713424, 'new_tag': False}, {'iid': 6853641, 'title': '郑爽 我为我的鲁莽道歉', 'more': '17.1万', 'add_date': 1597739683, 'new_tag': False}, {'iid': 6853818, 'title': '挂19科最后正常毕业', 'more': '16.7万', 'add_date': 1597743794, 'new_tag': False}, {'iid': 6851173, 'title': '你希望哪支乐队来《乐夏》', 'more': '14.4万', 'add_date': 1597652115, 'new_tag': False}, {'iid': 6853320, 'title': '郑秀晶与SM解约', 'more': '13.9万', 'add_date': 1597731446, 'new_tag': False}, {'iid': 6853895, 'title': '王岳伦又爆与女子亲密照', 'more': '12.8万', 'add_date': 1597745801, 'new_tag': False}, {'iid': 6853556, 'title': '剩饭菜超重取消奖学金', 'more': '12.5万', 'add_date': 1597737523, 'new_tag': False}, {'iid': 6853403, 'title': '东北大爷卖苞米棒子走红', 'more': '11.5万', 'add_date': 1597733330, 'new_tag': False}, {'iid': 6853640, 'title': '紫罗兰永恒花园定档', 'more': '11.1万', 'add_date': 1597739683, 'new_tag': False}, {'iid': 6853250, 'title': '西游记81难通关图', 'more': '10.8万', 'add_date': 1597729577, 'new_tag': False}, {'iid': 6852878, 'title': '巴萨主帅塞蒂恩下课', 'more': '10.6万', 'add_date': 1597719278, 'new_tag': False}, {'iid': 6852778, 'title': '中铁建董事长坠楼身亡', 'more': '10.2万', 'add_date': 1597717464, 'new_tag': False}, {'iid': 6853817, 'title': '中国奶茶图鉴', 'more': '8.4万', 'add_date': 1597743794, 'new_tag': False}], 'attrs': {'cn': '贴吧', 'display': 10}}]}}}
    baidulist=r1.json()
    # print(baidulist['data']['site'])
    baidunews=baidulist['data']['site']['subs']
    # print(baidunews)

    # for i in baidunews:
    #     print('--------------------------',i['items'])
    #     for x in i['items']:
    #         print(x)
    # print(baidunews[0]['items'])
    print('百度排行榜')
    for i,x in zip(baidunews[0]['items'],range(1,50)):
        print(x,i['title'],i['more'])

def weibo():
    ur2='https://www.anyknew.com/api/v1/sites/weibo'
    r2=requests.get(ur2)
    # print(r2.json())
    # baidulist={'status': 0, 'msg': 'success', 'data': {'site': {'site': 'weibo', 'attrs': {'cn': '微博', 'logo': 'https://f0cdn.anyknew.com/static/logo/weibo.png', 'url': 'https://www.weibo.com', 'iter': 43763}, 'subs': [{'items': [{'iid': 6855432, 'title': '金莎 很糊的艺人才有自由', 'more': '3169833', 'add_date': 1597809249, 'new_tag': False}, {'iid': 6855537, 'title': '乐山大佛脚趾露出', 'more': '1813811', 'add_date': 1597812857, 'new_tag': False}, {'iid': 6855518, 'title': '牛奶咖啡斥何洛洛新歌抄袭', 'more': '1742307', 'add_date': 1597811906, 'new_tag': False}, {'iid': 6855536, 'title': '赵丽颖慵懒风大片', 'more': '1178228', 'add_date': 1597812857, 'new_tag': False}, {'iid': 6855097, 'title': '特朗普反击奥巴马夫人', 'more': '936264', 'add_date': 1597801643, 'new_tag': False}, {'iid': 6855282, 'title': '律师谈老人被狗绳绊倒身亡', 'more': '768618', 'add_date': 1597805895, 'new_tag': False}, {'iid': 6855019, 'title': '五人出游一人还事件舅舅起诉外甥女', 'more': '672708', 'add_date': 1597800006, 'new_tag': False}, {'iid': 6855138, 'title': '浙江省考成绩', 'more': '648557', 'add_date': 1597802574, 'new_tag': False}, {'iid': 6855021, 'title': '王鹤棣', 'more': '647157', 'add_date': 1597800006, 'new_tag': False}, {'iid': 6855516, 'title': '密室大逃脱', 'more': '645563', 'add_date': 1597811906, 'new_tag': False}, {'iid': 6854748, 'title': '被狗绳绊倒身亡老人亲友发声', 'more': '530510', 'add_date': 1597792922, 'new_tag': False}, {'iid': 6855315, 'title': '洪水漫上重庆主城', 'more': '420678', 'add_date': 1597806704, 'new_tag': False}, {'iid': 6854746, 'title': '谢园去世', 'more': '403749', 'add_date': 1597792922, 'new_tag': False}, {'iid': 6855431, 'title': '刘欣揭孟晚舟案背后隐情', 'more': '336259', 'add_date': 1597809249, 'new_tag': False}, {'iid': 6854857, 'title': '中国医师节', 'more': '329947', 'add_date': 1597796399, 'new_tag': False}, {'iid': 6855517, 'title': 'NBA', 'more': '329421', 'add_date': 1597811906, 'new_tag': False}, {'iid': 6855463, 'title': '利拉德logo shot', 'more': '327883', 'add_date': 1597810262, 'new_tag': False}, {'iid': 6855464, 'title': '杨幂苹果衬衫', 'more': '326550', 'add_date': 1597810262, 'new_tag': False}, {'iid': 6855608, 'title': '德云社团建', 'more': '324181', 'add_date': 1597815650, 'new_tag': True}, {'iid': 6855284, 'title': '广东7名驴友被冲走3人溺亡', 'more': '323795', 'add_date': 1597805895, 'new_tag': False}, {'iid': 6855334, 'title': '美国民主党正式提名拜登为总统候选人', 'more': '270830', 'add_date': 1597807505, 'new_tag': False}, {'iid': 6855333, 'title': '霍华德把篮筐扣歪', 'more': '270711', 'add_date': 1597807505, 'new_tag': False}, {'iid': 6855582, 'title': '刘佳', 'more': '269934', 'add_date': 1597814674, 'new_tag': True}, {'iid': 6855581, 'title': '张晋跳搞不定舞', 'more': '269663', 'add_date': 1597814674, 'new_tag': True}, {'iid': 6854744, 'title': '章绍伟道歉', 'more': '269169', 'add_date': 1597792922, 'new_tag': False}, {'iid': 6855316, 'title': '井底蛙顺着绳子奋力往岸上爬', 'more': '268461', 'add_date': 1597806704, 'new_tag': False}, {'iid': 6850576, 'title': '股市', 'more': '268122', 'add_date': 1597635760, 'new_tag': False}, {'iid': 6855077, 'title': '尚雯婕拍的武汉', 'more': '267666', 'add_date': 1597800913, 'new_tag': False}, {'iid': 6855245, 'title': '刘亦菲花木兰武术训练', 'more': '267480', 'add_date': 1597805180, 'new_tag': False}, {'iid': 6855607, 'title': '乌克兰巨大水母群覆盖海面', 'more': '267011', 'add_date': 1597815650, 'new_tag': True}, {'iid': 6855580, 'title': '雨后出现云横秦岭景观', 'more': '259946', 'add_date': 1597814674, 'new_tag': True}, {'iid': 6854797, 'title': '马里总统总理被军人扣留', 'more': '258422', 'add_date': 1597794881, 'new_tag': False}, {'iid': 6855140, 'title': '晓明跳舞像零件有点劳损的机器人', 'more': '257763', 'add_date': 1597802574, 'new_tag': False}, {'iid': 6854747, 'title': '戚薇黑皇后造型', 'more': '251437', 'add_date': 1597792922, 'new_tag': False}, {'iid': 6854965, 'title': '香港奶粉', 'more': '242912', 'add_date': 1597798988, 'new_tag': False}, {'iid': 6855020, 'title': '缓解头痛的小方法', 'more': '191578', 'add_date': 1597800006, 'new_tag': False}, {'iid': 6855314, 'title': '新版新冠诊疗方案明确潜伏期传染性', 'more': '172176', 'add_date': 1597806704, 'new_tag': False}, {'iid': 6855389, 'title': '陈凯歌悼念谢园', 'more': '169115', 'add_date': 1597808307, 'new_tag': False}, {'iid': 6855647, 'title': '25岁女舵手7年海上航行1200多天', 'more': '165401', 'add_date': 1597816642, 'new_tag': True}, {'iid': 6854966, 'title': '秦皇岛昌黎海边出现海市蜃楼', 'more': '156054', 'add_date': 1597798988, 'new_tag': False}, {'iid': 6855646, 'title': '港交所取消今日盘前交易', 'more': '154350', 'add_date': 1597816642, 'new_tag': True}, {'iid': 6855645, 'title': '张定宇张文宏陶勇获中国医师奖', 'more': '152646', 'add_date': 1597816642, 'new_tag': True}, {'iid': 6855644, 'title': '银龙广场', 'more': '148722', 'add_date': 1597816642, 'new_tag': True}, {'iid': 6855643, 'title': '医生版无价之姐', 'more': '145548', 'add_date': 1597816642, 'new_tag': True}, {'iid': 6855579, 'title': '医护洪水中转移200箱病历', 'more': '145317', 'add_date': 1597814674, 'new_tag': True}, {'iid': 6854448, 'title': '孟佳 我真的上台了', 'more': '145304', 'add_date': 1597764529, 'new_tag': False}, {'iid': 6855496, 'title': '开拓者击败湖人', 'more': '136754', 'add_date': 1597811151, 'new_tag': False}], 'attrs': {'cn': '热搜榜', 'display': 10}}]}}}
    weibolist=r2.json()
    # print(baidulist['data']['site'])
    weibolist=weibolist['data']['site']['subs']
    # print(baidunews)
    # print(weibolist[0]['items'])
    print('微博排行榜')
    for i,x in zip(weibolist[0]['items'],range(1,50)):
        more = "%.2f" % (int(i['more']) / 10000)
        print(x,i['title'],more+'万')

#东方财富网
def eastmoney():
    ur3='https://www.anyknew.com/api/v1/sites/eastmoney'
    r3=requests.get(ur3)
    dongfanglist=r3.json()
    dfcf=dongfanglist['data']['site']['subs'][0]['items']
    print('财经新闻排行')
    j=1
    for i in dfcf:
        print(j,i['title'])
        j +=1



#汽车之家
def autohome():
    ur3='https://www.anyknew.com/api/v1/sites/autohome'
    r3=requests.get(ur3)
    dongfanglist=r3.json()
    dfcf=dongfanglist['data']['site']['subs'][0]['items']
    print('汽车新闻排行')
    j=1
    for i in dfcf:
        print(j,i['title'])
        j +=1


baidu()
eastmoney()
autohome()


