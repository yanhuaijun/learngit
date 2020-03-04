# coding=utf-8
import selenium
from appium import webdriver
import  time

desired_caps = {}
desired_caps['deviceName']="72a145a"
desired_caps['automationName']='Appium'
desired_caps['platformName'] = 'Android'       #安卓系统
desired_caps['platformVersion'] = '8.0.1'      #安卓系统的版本
desired_caps['deviceName'] = 'Mi_Note_3'         #设备型号 Android Emulator（模拟器）
desired_caps['appPackage'] = 'com.wuba'        #打开应用程序的包名 58同城
desired_caps['appActivity'] = '.home.activity.HomeActivity'  #程序的首页


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)    #appuim 上面的那个ip

# desired_caps['unicodeKeyboard']=True,#使用unicodeKeyboard的编码方式来发送字符串
# desired_caps['resetKeyboard']=True#将键盘给隐藏起来

time.sleep(6)
print("打开APP")
driver.find_element_by_name("我的").click()   #点击个人中心
time.sleep(1)
driver.find_element_by_name("首页").click()       #点击首页
time.sleep(1)
driver.find_element_by_name("发现").click()       #点击发现
time.sleep(1)
driver.find_element_by_name("消息").click()       #点击消息
