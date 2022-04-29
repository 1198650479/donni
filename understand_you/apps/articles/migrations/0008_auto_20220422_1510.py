# Generated by Django 3.2.3 on 2022-04-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_article_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_collection',
            field=models.PositiveIntegerField(default=0, verbose_name='文章收藏数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_comments_num',
            field=models.PositiveIntegerField(default=0, verbose_name='文章评论数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_forward',
            field=models.PositiveIntegerField(default=0, verbose_name='文章转发数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_like',
            field=models.PositiveIntegerField(default=0, verbose_name='文章点赞数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_views',
            field=models.PositiveIntegerField(default=0, verbose_name='文章浏览量'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user_id',
            field=models.PositiveIntegerField(verbose_name='发布者ID'),
        ),
    ]