# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-06 04:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0015_auto_20180105_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='level',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='topic',
        ),
    ]
