# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-21 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0017_auto_20180320_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='place',
            field=models.CharField(max_length=50000, null=True),
        ),
    ]
