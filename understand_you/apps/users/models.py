from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=11, unique=True, verbose_name=u'手机号')
    user_head = models.ImageField(default='https://img0.baidu.com/it/u=324179460,1196659069&fm=253&fmt=auto&app=138&f=JPEG?w=400&h=400', verbose_name="用户头像")
    user_name = models.CharField(max_length=50, default='普通用户', verbose_name=u'昵称')
    password = models.CharField(max_length=100, verbose_name=u'密码')
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='female', verbose_name=u'性别')
    birthday = models.DateField(verbose_name=u'生日', null=True)
    interest = models.CharField(max_length=20, blank='null',verbose_name=u'兴趣')
    personal_signature = models.CharField(max_length=100, default=u'为了爱与和平~', verbose_name=u'个性签名')
    address = models.CharField(max_length=50, null=True, verbose_name=u'地址')
    user_fans_num = models.CharField(max_length=100, default=0, verbose_name=u'粉丝数')
    follow_num = models.CharField(max_length=100, default=0, verbose_name=u'关注数')
    user_collection = models.CharField(max_length=100, default=0, verbose_name=u'用户收藏数')
    browsing_history = models.CharField(max_length=100, default=0, verbose_name=u'浏览历史数')

    class Meta:
        db_table = 'tb_user'
        verbose_name = u'用户'
        verbose_name_plural = verbose_name