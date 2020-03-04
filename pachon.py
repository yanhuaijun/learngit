
import requests
import urllib
from bs4 import BeautifulSoup

url1="http://www.59xihuan.cn/meiwen/201905/57567.html"

a = requests.get(url1)
a.encoding = a.apparent_encoding
# print(a.text)
soup = BeautifulSoup(a.text, features='html.parser')
print(soup.h4.text)
print(soup.find(class_="pic_text0").text)