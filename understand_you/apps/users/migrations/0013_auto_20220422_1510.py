# Generated by Django 3.2.3 on 2022-04-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_userfollow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='browsing_history',
            field=models.PositiveIntegerField(default=0, verbose_name='浏览历史数'),
        ),
        migrations.AlterField(
            model_name='user',
            name='follow_num',
            field=models.PositiveIntegerField(default=0, verbose_name='关注数'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_collection',
            field=models.PositiveIntegerField(default=0, verbose_name='用户收藏数'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_fans_num',
            field=models.PositiveIntegerField(default=0, verbose_name='粉丝数'),
        ),
    ]
