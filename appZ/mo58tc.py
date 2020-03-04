# coding=utf-8
import selenium
from appium import webdriver
import  time

desired_caps = {}
desired_caps['deviceName']="72a145a"
desired_caps['automationName']='Appium'
desired_caps['platformName'] = 'Android'       #安卓系统
desired_caps['platformVersion'] = '5.1.1'      #安卓系统的版本
desired_caps['deviceName'] = 'Android Emulator'         #设备型号 Android Emulator（模拟器）
desired_caps['appPackage'] = 'com.wuba'        #打开应用程序的包名 58同城
desired_caps['appActivity'] = '.home.activity.HomeActivity'  #程序的首页

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)    #appuim 上面的那个ip

# capabilities['platformName'] = 'Android'
# capabilities['deviceName'] = 'Android Emulator'
# capabilities['appPackage'] = 'com.example.android.contactmanager'
# capabilities['appActivity'] = '.ContactManager'
# capabilities['app'] = PATH('./apps/ContactManager.apk')
# capabilities['unicodeKeyboard'] = 'True'
# capabilities['resetKeyboard'] = 'True'
# driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
# capabilities['platformVersion'] = '5.1'

# desired_caps['unicodeKeyboard']=True,#使用unicodeKeyboard的编码方式来发送字符串
# desired_caps['resetKeyboard']=True#将键盘给隐藏起来

time.sleep(6)
print("打开APP")
driver.find_element_by_name("首页").click()   #点击个人中心
time.sleep(1.5)
driver.find_element_by_name("发现").click()       #点击首页
time.sleep(1.5)
driver.find_element_by_name("消息").click()       #点击发现
time.sleep(1.5)
driver.find_element_by_name("首页").click()       #点击消息
driver.get_window_size()
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
print(getSize())
#屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)
#屏幕向下滑动
def swipeDown(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    driver.swipe(x1, y1, x1, y2, t)

# 调用向上滑动
swipeUp(3000)
time.sleep(5)
# 调用向下滑动
swipeDown(2000)
time.sleep(5)

driver.press_keycode(3)
print("ture")
