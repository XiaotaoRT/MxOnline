# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-06-05 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_courseorg_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorg',
            name='tag',
        ),
    ]
