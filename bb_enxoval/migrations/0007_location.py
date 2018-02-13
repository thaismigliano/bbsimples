# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-14 02:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('bb_enxoval', '0006_state_acronym'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='bb_enxoval.City')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bb_enxoval.State')),
            ],
        ),
    ]