# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_enxoval', '0003_auto_20180113_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
