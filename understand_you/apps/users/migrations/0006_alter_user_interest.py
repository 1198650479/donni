# Generated by Django 3.2.3 on 2022-03-15 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_user_head'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='interest',
            field=models.CharField(blank=True, max_length=20, verbose_name='兴趣'),
        ),
    ]
