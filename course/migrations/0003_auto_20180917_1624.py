# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20180917_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=11, verbose_name='电话号码'),
        ),
    ]