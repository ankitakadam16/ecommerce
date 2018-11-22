# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0014_checkin_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkins', to='warehouse.Contract'),
        ),
    ]
