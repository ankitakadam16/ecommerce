# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0029_commodity_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='commodityFor',
            field=models.CharField(max_length=50000, null=True),
        ),
    ]
