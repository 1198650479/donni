# Generated by Django 3.2.3 on 2022-03-18 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_article_label'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_fabulous',
            new_name='article_like',
        ),
    ]
