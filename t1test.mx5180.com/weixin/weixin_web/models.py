from django.db import models

# Create your models here.
class wxuser(models.Model): #微信用户表
    unionid = models.CharField(max_length=32)
    openid = models.CharField(max_length=32)
    stats = models.CharField(max_length=32)
    userid = models.CharField(max_length=32)
    create_time=models.CharField(max_length=32)
    upeate_time =models.CharField(max_length=32)
    class Meta:
        db_table = "wxuser"