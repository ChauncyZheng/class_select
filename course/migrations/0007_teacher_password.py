# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-19 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20180918_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(default='123456', max_length=256, verbose_name='密码'),
        ),
    ]
