from django.db import models

# Create your models here.

class Article(models.Model):

    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=32, unique=True, verbose_name=u"文章标题")
    active_label = models.CharField(max_length=20, choices=(('notice', u'公告'), ('strategy', u'攻略'), ('talk', u'趣谈')), unique=True, verbose_name=u'文章类型')
    article_img = models.ImageField(verbose_name=u"文章封面图")
    article_content = models.TextField(verbose_name=u"文章内容")
    article_uptime = models.DateTimeField(verbose_name=u"发布时间")
    user_id = models.CharField(max_length=50, verbose_name=u"发布者ID")
    article_views = models.FloatField(default=0, verbose_name=u"文章浏览量")
    article_fabulous = models.FloatField(default=0, verbose_name=u"文章点赞数")
    article_collection = models.FloatField(default=0, verbose_name=u"文章收藏数")
    article_forward = models.FloatField(default=0, verbose_name=u"文章转发数")
    article_comments_num = models.FloatField(default=0, verbose_name=u"文章评论数")

    class Meta:
        db_table = 'articles'
        verbose_name = u'文章'
        verbose_name_plural = verbose_name