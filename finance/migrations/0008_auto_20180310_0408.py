# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-10 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_auto_20180310_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesheet',
            name='notes',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
