# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-11 22:25
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('bb_enxoval', '0007_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, sort=False, to='bb_enxoval.City'),
        ),
    ]