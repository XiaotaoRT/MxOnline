# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-06-07 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0008_teacher_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='lick_nums',
            new_name='click_nums',
        ),
    ]