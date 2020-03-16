from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
# Register your models here.
class UserType(models.Model):
    name = models.CharField(max_length=32)


class wxuser(models.Model): #微信用户表
    unionid = models.CharField(max_length=32)
    openid = models.CharField(max_length=32)
    stats = models.CharField(max_length=32)
    userid = models.CharField(max_length=32)
    create_time=models.CharField(max_length=32)
    upeate_time =models.CharField(max_length=32)


class UserInfo(models.Model): #用户表
    username = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    user_type = models.ForeignKey('UserType', on_delete=models.CASCADE, )
    create_by=models.CharField(max_length=32)
    create_date =models.CharField(max_length=32)
    upeate_by =models.CharField(max_length=32)
    upeate_date =models.CharField(max_length=32)

class User(models.Model): #用户表
    username = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    Mobile_phone=models.CharField(max_length=32)
    create_by=models.CharField(max_length=32)
    create_date =models.CharField(max_length=32)
    upeate_by =models.CharField(max_length=32)
    upeate_date =models.CharField(max_length=32)


class mood (models.Model):#心情文章表
    title=models.CharField(max_length=500)
    content=models.CharField(max_length=50000)
    create_by = models.CharField(max_length=32)
    create_date = models.CharField(max_length=32)
    upeate_by = models.CharField(max_length=32)
    upeate_date = models.CharField(max_length=32)

class Love (models.Model):#爱情文章表
    title=models.CharField(max_length=500)
    content=models.CharField(max_length=50000)
    create_by = models.CharField(max_length=32)
    create_date = models.CharField(max_length=32)
    upeate_by = models.CharField(max_length=32)
    upeate_date = models.CharField(max_length=32)

class Chicken_soup (models.Model):#鸡汤文章表
    title=models.CharField(max_length=500)
    content=models.CharField(max_length=50000)
    create_by = models.CharField(max_length=32)
    create_date = models.CharField(max_length=32)
    upeate_by = models.CharField(max_length=32)
    upeate_date = models.CharField(max_length=32)

class Sentimental(models.Model):  # 伤感文章表
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=50000)
    create_by = models.CharField(max_length=32)
    create_date = models.CharField(max_length=32)
    upeate_by = models.CharField(max_length=32)
    upeate_date = models.CharField(max_length=32)

class Struggle(models.Model):  # 奋斗文章表
    title = models.CharField(max_length=500)#标题
    content = models.CharField(max_length=50000)#内容
    create_by = models.CharField(max_length=32)#创建者
    create_date = models.CharField(max_length=32)#创建时间
    upeate_by = models.CharField(max_length=32)#修改者
    upeate_date = models.CharField(max_length=32)#修改时间

class music(models.Model):  # 音乐表
    title = models.CharField(max_length=500)  # 标题
    author = models.CharField(max_length=500)  # 作者
    play_url=models.CharField(max_length=50000)  # 播放地址
    picture_url=models.CharField(max_length=50000)  # 图片地址