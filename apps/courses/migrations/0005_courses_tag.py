# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-06-05 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_courses_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='tag',
            field=models.CharField(default='', max_length=10, verbose_name='课程标签'),
        ),
    ]