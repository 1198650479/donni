from django.db import models

# Create your models here.
class Comments(models.Model):

    comment_id = models.AutoField(primary_key=True, verbose_name=u"评论id")
    comment_user_id = models.CharField(max_length=20, verbose_name=u"评论人ID")
    comment_content = models.TextField(verbose_name=u"评论内容")
    comment_like = models.PositiveIntegerField(default=0, verbose_name=u"评论点赞数")
    comment_reply = models.PositiveIntegerField(default=0, verbose_name=u"评论回复数")
    comment_date = models.DateField(verbose_name=u"评论时间")
    comment_label = models.CharField(max_length=20, default="comment", verbose_name=u"被评论类型(文章/评论)")
    article_id = models.CharField(max_length=20, verbose_name=u"被评论文章id")

    class Meta:
        db_table = 'article_comments'
        verbose_name = u'文章评论'
        verbose_name_plural = verbose_name

class Reply(models.Model):

    reply_id = models.AutoField(primary_key=True)
    comment_id = models.CharField(max_length=20, verbose_name=u"被回复评论id")
    reply_user_id = models.CharField(max_length=20, verbose_name=u"回复者id")
    reply_comment = models.TextField(verbose_name=u"回复内容")
    reply_like = models.FloatField(default=0, verbose_name=u"回复点赞数")
    reply_date = models.DateField(verbose_name=u"回复时间")

    class Meta:
        db_table = 'comment_reply'
        verbose_name = u'回复'
        verbose_name_plural = verbose_name