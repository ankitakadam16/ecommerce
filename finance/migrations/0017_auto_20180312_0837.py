# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0016_invoice_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensesheet',
            name='approvalMatrix',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='expensesheet',
            name='approvalStage',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='expensesheet',
            name='dispensed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='expensesheet',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='expensesheet',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenseSheet', to='finance.Transaction'),
        ),
    ]
