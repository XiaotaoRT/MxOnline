# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-06-08 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180602_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '找回密码'), ('update_email', '新增邮箱')], max_length=15, verbose_name='验证码类型'),
        ),
    ]
