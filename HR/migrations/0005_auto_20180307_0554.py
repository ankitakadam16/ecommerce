# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0004_auto_20180305_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='bankDetais',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
