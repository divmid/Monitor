from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, verbose_name="用户名", unique=True)
    password = models.CharField(max_length=32, verbose_name="密码")
    dingding_token = models.TextField(null=True, blank=True, verbose_name="钉钉群地址")
    polling_interval = models.IntegerField(verbose_name="轮询间隔(秒)", null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)



class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name="用户主键")
    name = models.CharField(max_length=32, verbose_name="股票名称")
    stock_code = models.CharField(max_length=32, verbose_name="股票代码")
    max_proportion = models.IntegerField(verbose_name="涨幅比例")
    min_proportion = models.IntegerField(verbose_name="跌幅比例")
    create_date = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
