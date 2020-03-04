from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://t.oa.quanhoo.com/?#/login')
time.sleep(2)

driver.find_element_by_name("logincode").send_keys("13066875865")
driver.find_element_by_name("pwd").send_keys("aa123456")

driver.find_element_by_xpath("//*[@id='app']/div/form/div[3]/div/button").click() #点击登录
time.sleep(3)
a = driver.find_element_by_xpath('/html/body/div[2]/p').text
print(a)

# a = driver.find_element_by_css_selector( '.layui-layer-content.layui-layer-padding').get_attribute('textContent')
# print(a)


# driver.find_element_by_xpath("//span[text()='CRM']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='客户审核']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//div[@class='el-table__fixed-right']/div[@class='el-table__fixed-body-wrapper']/table/tbody/tr[1]/..//button[1]").click()
# #driver.find_element_by_xpath("//*[@id='gMain']/div[2]/div/div[4]/div[5]/div[2]/table/tbody/tr[1]/td[27]/div/div/button[1]/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='通过审核']").click()
# time.sleep(2)
# #driver.find_element_by_css_selector("[class='el-button el-button--default el-button--small el-button--primary ']").click()
#
# # al = driver.switch_to.alert()
# # time.sleep(1)
# # print("----------------------------"+a1.text)
# # al.accept()


# driver.close()