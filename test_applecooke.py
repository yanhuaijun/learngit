from selenium  import webdriver
import  time
from selenium.webdriver.common.by import By
# driverOptions = webdriver.ChromeOptions()
#
# driverOptions.add_argument(r"C:\Users\LG198900\AppData\Local\Google\Chrome\User Data")
# driver= webdriver.Chrome("chromedriver",0,driverOptions)

driver=webdriver.Chrome()
# driver.maxmize_window()
url1='http://t-sz.oa.quanhoo.com'
url2='https://reportaproblem.apple.com/'
driver.get(url2)
print('打开网页')
time.sleep(6)
driver.delete_all_cookies()
time.sleep(2)
cookies_list1=[{'domain': 't-sz.oa.quanhoo.com', 'httpOnly': False, 'name': 'Admin-Token', 'path': '/', 'secure': False, 'value': '2020-03-30%2022:58:40738374'}, {'domain': 't-sz.oa.quanhoo.com', 'httpOnly': True, 'name': 'SESSION', 'path': '/', 'secure': False, 'value': '1ed79c8f-3ee8-4817-a501-08a1e7065571'}, {'domain': '.oa.quanhoo.com', 'httpOnly': False, 'name': 'Hm_lpvt_8479090c3350e17a831341dac78f8aa5', 'path': '/', 'secure': False, 'value': '1585580312'}, {'domain': 't-sz.oa.quanhoo.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': False, 'value': 'B8C8BBE56D9AD8D2FB93B69D5A393F27'}, {'domain': '.oa.quanhoo.com', 'expiry': 1617116312, 'httpOnly': False, 'name': 'Hm_lvt_8479090c3350e17a831341dac78f8aa5', 'path': '/', 'secure': False, 'value': '1585580312'}]
cookies_list2=[{'domain': '.reportaproblem.apple.com', 'httpOnly': True, 'name': 'selfserv_c', 'path': '/', 'secure': True, 'value': 'CHN'}, {'domain': '.reportaproblem.apple.com', 'httpOnly': True, 'name': 'selfserv_a', 'path': '/', 'secure': True, 'value': 'MJN87kay0BGaq4WyAbjROEHb7j0tWo3V9ZTCvAock9Y94qT1bmuLwwzHmEz8nvX5CHguMSoFYvgxbPJwn8TgtUv5iRD7brdU1WtFQpmxfSfvj17fx9J9LhW1gXvr9tQ8/32/'}, {'domain': 'reportaproblem.apple.com', 'httpOnly': True, 'name': 'dqsid', 'path': '/', 'secure': True, 'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODU2NDEyNzUsImp0aSI6IjF4c0t4VFVQQXQtMWNuN3ZTeUNXN0EifQ.C6Egng3ZARu07KhKAXP5ck_uGE_Ev_4_WzwFwdip0kE'}, {'domain': '.apple.com', 'httpOnly': True, 'name': 'myacinfo', 'path': '/', 'secure': True, 'value': 'DAWTKNV21422cfa9f89248750f3ad29458e16aa709ba3fd15fa01f09126628d084e728007aa745f0fa7cff53bd00f4f1734c838e2d6f3568005bc7373964125ebc81a704098452f4d76c2ffa7168fc43378e1d29c55f998b9c047e4172a2f839666367369b16995e37cd5ee4dc977359b7d1ca8ca8687ff0e928131501f8db310f5db8a41e77eef6415980669dc419a45b8b7fef7cc95dbee981d80556c70f01f4097f9463e33403a70425a9f03d8cc47ac3eef780cd696929fde26314b80539ce9d0855d53f8ea6e612ba8433d20bdeb4de681576a48e502275bd8472814662f2864af610132155f43fb7e72b091df32c2e907a65383733393964353061313861656164626438616263383937373534656132313463366532353639MVRYV2'}, {'domain': '.reportaproblem.apple.com', 'httpOnly': True, 'name': 'itspod', 'path': '/', 'secure': True, 'value': '31'}, {'domain': '.reportaproblem.apple.com', 'httpOnly': True, 'name': 'selfserv_s', 'path': '/', 'secure': True, 'value': '143465'}, {'domain': '.apple.com', 'httpOnly': True, 'name': 'site', 'path': '/', 'secure': True, 'value': 'CHN'}, {'domain': '.apple.com', 'httpOnly': False, 'name': 'ccl', 'path': '/', 'secure': False, 'value': '93is90L60MGunYxMyhU8lA=='}, {'domain': '.apple.com', 'httpOnly': False, 'name': 'geo', 'path': '/', 'secure': False, 'value': 'CN'}, {'domain': '.reportaproblem.apple.com', 'httpOnly': True, 'name': 'selfserv_l', 'path': '/', 'secure': True, 'value': 'zh-CN'}, {'domain': '.apple.com', 'expiry': 1648713840, 'httpOnly': True, 'name': 'dslang', 'path': '/', 'secure': True, 'value': 'CN-ZH'}]
cookies_lg=[{'domain': '.reportaproblem.apple.com', 'httpOnly': True, 'name': 'selfserv_c', 'path': '/', 'secure': True, 'value': 'CHN'}, {'domain': '.reportaproblem.apple.com', 'httpOnly': True, 'name': 'selfserv_a', 'path': '/', 'secure': True, 'value': 'IUzQC/iRBfLeIaDtoFKgdSphkO9AtRBs6lIkVMR50xjGH1yXFqXtkvWzdDTlIJI8LW3y4UdyNYfNuReDEEnhiLp+zKL0xERYapj+q3pg728Ih9N2wTYGXHJ8RAihdJuS6QaJ'}, {'domain': 'reportaproblem.apple.com', 'httpOnly': True, 'name': 'dqsid', 'path': '/', 'secure': True, 'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODU2NDY3ODksImp0aSI6Ik1PbW9SalBBNUstY0d1ZmFfOXBrSXcifQ.xYkm7apDKmVkWCRlBaaMMP2FxAhrqmzNkV6d0uMfu_g'}, {'domain': '.apple.com', 'httpOnly': True, 'name': 'myacinfo', 'path': '/', 'secure': True, 'value': 'DAWTKNV24a459f576a459055444189f49e07543656f4c9e2467f274ca4a378d496a7e5205ccb02388e2a157bbb8da6559698e0f2abe3ad1e92d640f2857023c0089f95c5e445302d8f78d04ddeeb47a43a42621a26f72abec8bea35f9368be46ba74195bcbc5f1b5a02fb0f7c54886a65336288b178bb89ecb21a53f99732535b0bbd8ca2dcafd09d2c4bd2e52e8157d957e39fa8bf0811bbdec347f2a86ebfbc64b4fa72f90b5984769214356a5e898ad17731afdde5734ba917f44a8625a928413199e26e4b9d68dc127ad7e7125462c03930de7410cc43c6057aa4dc5c8eb4b46102acd9d54277b9354f6637e4d91d35ad9bc763358088c8969bf71be249dc1ed90694956e0b239c4deb76695f525791f5174d7e08dee8977884ccb38620c8f73000b408d6da021ab50e111f412f149f8e2f86b4bf12a1f2028f7d396ca2346f2e38ff923fbaab85aded5f009559eb16147e5de198dd4f7cc7d9cccc2ba8a72b64e4e977f449a44ccb1ac4dc0bd4c98fa4ea218e354e83862dff5e81cf2dae249b7af63656638656163313262313864303066353132383937626334366563653037356536336637626233MVRYV2'}, {'domain': '.reportaproblem.apple.com', 'httpOnly': True, 'name': 'itspod', 'path': '/', 'secure': True, 'value': '32'}, {'domain': '.reportaproblem.apple.com', 'httpOnly': True, 'name': 'selfserv_s', 'path': '/', 'secure': True, 'value': '143465'}, {'domain': '.apple.com', 'httpOnly': True, 'name': 'site', 'path': '/', 'secure': True, 'value': 'CHN'}, {'domain': '.apple.com', 'httpOnly': False, 'name': 'ccl', 'path': '/', 'secure': False, 'value': 'Pu/hZX/SYSDCDWrdrykYjQ=='}, {'domain': '.apple.com', 'httpOnly': False, 'name': 'geo', 'path': '/', 'secure': False, 'value': 'CN'}, {'domain': '.reportaproblem.apple.com', 'httpOnly': True, 'name': 'selfserv_l', 'path': '/', 'secure': True, 'value': 'zh-CN'}, {'domain': '.apple.com', 'expiry': 1648713840, 'httpOnly': True, 'name': 'dslang', 'path': '/', 'secure': True, 'value': 'CN-ZH'}]


for cookie in cookies_lg:
    driver.add_cookie(cookie)
    print(cookie)

time.sleep(3)
driver.get(url2)
driver.refresh()
driver.find_element(By.CSS_SELECTOR, ".Apps").click()
time.sleep(1.5)
# 12 | click | css=.Subscriptions |  |
driver.find_element(By.CSS_SELECTOR, ".Subscriptions").click()
time.sleep(1.5)
# 13 | click | css=.Movies |  |
driver.find_element(By.CSS_SELECTOR, ".Movies").click()
time.sleep(1.5)
# 14 | click | css=.TVShows |  |
driver.find_element(By.CSS_SELECTOR, ".TVShows").click()
time.sleep(1.5)
# 15 | click | css=.Music |  |
driver.find_element(By.CSS_SELECTOR, ".Music").click()
time.sleep(1.5)
# 16 | click | css=.Books |  |
driver.find_element(By.CSS_SELECTOR, ".Books").click()



#
# cookieBefore = driver.get_cookies()
# print(cookieBefore)
# driver.find_element_by_name('logincode').send_keys('13066875865')
# time.sleep(1)
#
# driver.find_element_by_name('pwd').send_keys('123456')
# time.sleep(4)
#
# # driver.find_element_by_link_text('登录').click()
# time.sleep(3)
# cookies = driver.get_cookies()
# print(driver.get_cookies())





'''
driver=webdriver.Chrome()
# driver.maxmize_window()
driver.get("https://reportaproblem.apple.com/")
print('打开网页')
time.sleep(4)
driver.delete_all_cookies()
# cookie_dict={
#     'acn01':'xJ2oVggBbWCXpl/LRP8aZhh1oRK/jnP+ABNBgfp3B3A=',
#     'ccl':'MPDfnryTW5aUcftTick95w==',
#     'dqsid':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODU1NzE4NDgsImp0aSI6Impjemp1T0FiNGgwLUktMXhBUF9VRUEifQ.4dKARG2xkfn28rDmyUy2N6vm2zQ73UtRmMhJBFY-wQ0',
#     'dslang':'CN-ZH',
#     'geo':'CN',
#     'itspod':'31',
#     'myacinfo':'DAWTKNV2325b231d7f023def6b4fae41dc7f31bed9fcb160b142220df67f22d67205dc3f0b1d7108d660a0c4f1d1106c90d0903ecddcb2fd37289138a879ec6636a9095c3fe675bb924291d2f095d001e262f422d1a537df97b3b75835874171cd2a551aeb0891b52375f42007760e02d3a9ab304b9aa6f60436b920c52aefc7d80738ab764b69c932c3da95d46ca5f5364c3a8bc905a80568bede18651ce1426810fa9c13c01b963f52328f5b86e2e8dcb6a60e2c514cec888d7ce7a7f97591be7b8dca5c7f37d983bbb15bd1940b1c0bb98a58c930ab526e15ff515f5331ccc59fee1476d071d10d23f698ec797df7a749b282574d5a942d6f53cb186a0c2fe9465a1538313037343534356138643232613031643062383366666166613932396635383538306161373232MVRYV2',
#     'selfserv_a':'YwQ9ATSPP4VVXWhIdc2krZPepgiroE3IuVZNE5PxNbptSPt605LxxMO8rHIDFllArBZfKSYy9iiY74l3YLndULLXgJktJPjItSyMxzsbJWTXiB6BZWxdCSOiJkiMZkgHcJ0v',
#     'selfserv_c':'CHN',
#     'selfserv_l':'zh-CN',
#     'selfserv_s':'143465',
#     'site':'CHN',
# }

cookies={
    'value':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODU1NzE4NDgsImp0aSI6Impjemp1T0FiNGgwLUktMXhBUF9VRUEifQ.4dKARG2xkfn28rDmyUy2N6vm2zQ73UtRmMhJBFY-wQ0',
    'name':'dqsid',

}




driver.add_cookie(cookie_dict=cookies)
time.sleep(2)

driver.refresh()
time.sleep(6)
print('hhhhhh')
'''
# driver.find_element_by_class_name('force-ltr form-textbox form-textbox-text').send_keys('563292370@qq.com')

# driver.find_element_by_xpath('//*[@id="account_name_text_field"]').send_keys('563292370@qq.com')
# driver.find_element_by_css_selector(id="account_name_text_field").send_keys('111')
# driver.find_element_by_id('account_name_text_field').send_keys('111')

