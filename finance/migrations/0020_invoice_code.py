# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0019_auto_20180315_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='code',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
