# Generated by Django 3.2.3 on 2022-03-07 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220307_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='普通用户', max_length=50, verbose_name='昵称'),
        ),
    ]