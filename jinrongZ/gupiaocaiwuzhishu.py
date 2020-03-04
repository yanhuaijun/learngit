# coding: utf-8 ##股票财务数据指标分析
import requests,json,time
from bs4 import BeautifulSoup

# headers = {'Accept': "application/json, text/plain, */*",
#                'Accept-Encoding': 'gzip, deflate, br',
#                'Accept-Language': 'zh-CN,zh;q=0.9',
#                'Cache-Control': "no-cache",
#                'Host': 'stock.xueqiu.com',
#                 'Connection': 'keep-alive',
#             "Origin":"https://xueqiu.com",
#             "Referer":"https://xueqiu.com/snowman/S/SZ002746/detail",
#            'Pragma':'no-cache',
#            # 'Upgrade-Insecure-Requests':'1',
#            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400',
#            }
# Cookie={"xq_a_token":"01d9e7361ed17caf0fa5eff6465d1c90dbde9ae2",
#         "xqat":"a664afb60c7036c7947578ac1a5860c4cfb6b3b5",
#         "xq_r_token":"01d9e7361ed17caf0fa5eff6465d1c90dbde9ae2",
#         "u":"481583308312271",
#         "Hm_lvt_1db88642e346389874251b5a1eded6e3":"1583308313",
#         "device_id":"24700f9f1986800ab4fcc880530dd0ed",
#         "s":"ch11w3cxoi",
#         "Hm_lpvt_1db88642e346389874251b5a1eded6e3":"1583308362",
#         "cookiesu":"661583308362180"
#         }
headers={"Accept":"application/json, text/plain, */*",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
"Cookie":"xq_a_token=a664afb60c7036c7947578ac1a5860c4cfb6b3b5; xqat=a664afb60c7036c7947578ac1a5860c4cfb6b3b5; xq_r_token=01d9e7361ed17caf0fa5eff6465d1c90dbde9ae2; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU4NTM2MjYwNywiY3RtIjoxNTgzMzA4MzA5MTM1LCJjaWQiOiJkOWQwbjRBWnVwIn0.pR1yWw1WIm2lPRm-sBLaZq4am0tcaBAOasBzjKCzO5Iair0kpatGFv8o0lP2y0Zvei2dessVyHS4HMhlPkdpbATwllzR6eSkou13oBj-BA65ZG3BJoTbsg3Rnd9XML4pNC7ReCceS_NtrRGURjSb-zCxoCCuamclpoaUT0Ig58ZIphTbRZc0uuMTuwslwZZVHLDow83XMiuJtlLu2bsGwD-rD7KFWFeod92tbUa269LErqCI-r-ghXJi2nRLDTu9xh0Cf5U-eTEzJVMIDSKDMl7m9b-3NJ1hxMBx16V6N0ZoMo7Mz2pKbRtTtQOTcOehmE7PkrTEhN_rmqwxxwmG7A; u=481583308312271; Hm_lvt_1db88642e346389874251b5a1eded6e3=1583308313; device_id=24700f9f1986800ab4fcc880530dd0ed; s=ch11w3cxoi; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1583308362; cookiesu=661583308362180",
"Host":"stock.xueqiu.com",
"Origin":"https://xueqiu.com",
"Pragma":"no-cache",
"Referer":"https://xueqiu.com/snowman/S/SZ300822/detail",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400",

   }

ur01="https://stock.xueqiu.com/v5/stock/finance/cn/indicator.json?symbol="
ur03="&type=all&is_detail=true&count=5&timestamp=1583308379981"

ur02=['sz002746','sh600150','sz000876']
for i in ur02:
    re=requests.get(ur01+i+ur03,headers=headers)
    # print(re.text)  #把str类型转为json
    # print(ur01+i+ur03)
    re1=json.loads(re.text)
    # print(type(re1))
    print(re1['data'])
    print('----------------------')
    print(re1['data']['quote_name'],i)
    jj=re1['data']['list'][0]
    # print("%.2f%%" %((jj['total_revenue'][0]/100000000)))   ## "%.2f%%"% a  保留两位小数%，  "%.2f"% a 只保留两位小数
    print('营业收入: '+str(("%.2f"%((jj['total_revenue'][0]/100000000)))+'亿'))
    print('营业收入同比增长: '+str(jj['operating_income_yoy'][0])+'%')
    print('净利润同比增长: '+str(jj['net_profit_atsopc_yoy'][0])+'%')
    print('资产负债率: '+str(jj['asset_liab_ratio'][0])+'%')
    time.sleep(0.5)
'''
接口字段解释
关键指标：
营业收入	24.87亿    total_revenue 

营业收入同比增长	41.38%   operating_income_yoy

净利润	6.47亿  net_profit_atsopc

净利润同比增长 194.29%  net_profit_atsopc_yoy

扣非净利润 6.10亿  net_profit_after_nrgal_atsolc

扣非净利润同比增长 227.38%  np_atsopc_nrgal_yoy

每股指标：
每股收益 1.39  basic_eps  1
	
每股净资产	6.34   np_per_share  0

每股资本公积金	1.95  capital_reserve

每股未分配利润	3.21  undistri_profit_ps

每股经营现金流	1.78   operate_cash_flow_ps

盈利能力：
净资产收益率 23.92%  avg_roe 

净资产收益率-摊薄 0.22%  ore_dlt

总资产报酬率 19.66%  net_interest_of_total_assets

人力投入回报率 312.20%   rop

销售毛利率 27.79% gross_selling_rate

销售净利率 27.51%  net_selling_rate

财务风险：
资产负债率 21.90%  asset_liab_ratio

流动比率 3.35 current_ratio

速动比率 1.04 quick_ratio

权益乘数 1.28 equity_multiplier

产权比率 0.29  equity_ratio   equity_ratio

股东权益比率 78.10%  holder_equity

现金流量比率 0.97   ncf_from_oa_to_total_liab

运营能力：
存货周转天数	52.90天   inventory_turnover_days

应收账款周转天数	6.08天  receivable_turnover_days

应付账款周转天数	27.73天  accounts_payable_turnover_days

现金循环周期	31.07天  cash_cycle  

营业周期58.99天  operating_cycle

总资产周转率0.71次  total_capital_turnover

存货周转率	5.10次 inventory_turnover

应收账款周转率	44.38次  account_receivable_turnover

应付账款周转率	9.74次  accounts_payable_turnover

流动资产周转率	1.01次  current_asset_turnover_rate

固定资产周转率 2.90次 fixed_asset_turnover_ratio

'''