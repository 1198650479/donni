# Generated by Django 3.2.3 on 2022-03-11 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='active_label',
            new_name='article_label',
        ),
    ]
