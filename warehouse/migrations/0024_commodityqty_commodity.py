# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-18 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0023_commodity_commodityqty'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodityqty',
            name='commodity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commoditypro', to='warehouse.Commodity'),
        ),
    ]
