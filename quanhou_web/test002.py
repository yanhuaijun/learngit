from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://t.oa.quanhoo.com/?#/login')
time.sleep(2)

driver.find_element_by_name("logincode").send_keys("13066875865")
driver.find_element_by_name("pwd").send_keys("aa123456")

driver.find_element_by_xpath("//*[@class='el-form-item']/div/button").click() #点击登录
driver.implicitly_wait(10)
driver.find_element_by_xpath("//span[text()='数据看板']").click()
time.sleep(5)
driver.find_element_by_xpath("//span[text()='CRM']").click()
time.sleep(5)
driver.find_element_by_xpath("//span[text()='客户审核']").click()
time.sleep(5)#el-table__fixed-right
aa=driver.find_element_by_xpath("//div[@class='el-table__fixed-right']/div[@class='el-table__fixed-body-wrapper']/table/tbody/tr[1]/..//button[1]").text
print(aa)
time.sleep(5)#//*[@id="gMain"]/div[2]/div/div[4]/div[5]/div[2]/table/tbody/tr[2]/td[27]/div/div/button[1]
driver.find_element_by_xpath("//*[@class='el-table__fixed-right']/div[2]/table/tbody/tr[2]/td[27]/div/div/button[1]").click()
#driver.find_element_by_xpath("//*[@id='gMain']/div[2]/div/div[4]/div[5]/div[2]/table/tbody/tr[1]/td[27]/div/div/button[1]/span").click()
time.sleep(5)
driver.find_element_by_xpath("//span[text()='通过审核']").click()
time.sleep(5)
#driver.find_element_by_css_selector("[class='el-button el-button--default el-button--small el-button--primary ']").click()
driver.find_element_by_xpath("//*[@class='el-input el-input--suffix']/input").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@class='el-input el-input--suffix is-focus']/input").send_keys("严怀军")
time.sleep(5)
driver.find_element_by_xpath("//span[text()='严怀军（子豪）']").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@class='el-dialog__wrapper memberTypeDialog']/div/div[3]/div/button[1]").click()#//*[@id="gMain"]/div[2]/div/div[4]/div/div[3]/div/button[1]/span
#driver.find_elements_by_css_selector("button>class.el-button el-button--default").click()#//*[@id="gMain"]/div[2]/div/div[4]/div/div[3]/div/button[1]/span
time.sleep(5)
# al = driver.switch_to.alert()
# time.sleep(1)
# print("----------------------------"+a1.text)
# al.accept()


# driver.close()