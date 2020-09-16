# coding: utf-8 爬取图片保存本地



import requests,os
url = 'http://t.oa.quanhoo.com/static/img/404.5f76e01.png'
list=['https://img.quanhoo.com/news/uploadImg/2019_07_15/s_15312019_07_15_11_46_51.jpg','https://img.quanhoo.com/news/uploadImg/2019_07_15/s_15302019_07_15_11_46_36.jpg','https://img.quanhoo.com/news/uploadImg/2019_07_15/s_15272019_07_15_11_45_17.jpg']
'''
语法：os.path.split('PATH')
PATH指一个文件的全路径作为参数：
如果给出的是一个目录和文件名，则输出路径和文件名
如果给出的是一个目录名，则输出路径和为空文件名
'''
for i in list:
    r = requests.get(i,stream=True)
    imgname=os.path.split(i)[1]
    imgname='图片'+imgname
    with open(imgname, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)

