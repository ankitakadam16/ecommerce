# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-05 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0019_checkin_awb'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='areaLength',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
    ]
