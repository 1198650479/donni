# Generated by Django 3.2.3 on 2022-03-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_article_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_belong',
            field=models.CharField(default='', max_length=20, verbose_name='文章所属'),
        ),
    ]