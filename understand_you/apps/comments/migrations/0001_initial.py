# Generated by Django 3.2.3 on 2022-03-23 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_user_id', models.CharField(max_length=20, verbose_name='评论人ID')),
                ('comment_content', models.TextField(verbose_name='评论内容')),
                ('comment_like', models.FloatField(default=0, verbose_name='评论点赞数')),
                ('comment_reply', models.FloatField(default=0, verbose_name='评论回复数')),
                ('comment_date', models.DateField(verbose_name='评论时间')),
                ('article_id', models.CharField(max_length=20, verbose_name='被评论文章id')),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
                'db_table': 'article_comments',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('reply_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_id', models.CharField(max_length=20, verbose_name='被回复评论id')),
                ('reply_user_id', models.CharField(max_length=20, verbose_name='回复者id')),
                ('reply_comment', models.TextField(verbose_name='回复内容')),
                ('reply_like', models.FloatField(default=0, verbose_name='回复点赞数')),
                ('reply_date', models.DateField(verbose_name='回复时间')),
            ],
            options={
                'verbose_name': '回复',
                'verbose_name_plural': '回复',
                'db_table': 'comment_reply',
            },
        ),
    ]
