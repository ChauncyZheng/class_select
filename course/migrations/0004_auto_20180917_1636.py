# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20180917_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='describe',
            field=models.TextField(max_length=200, verbose_name='课程描述'),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(max_length=200, verbose_name='问题内容'),
        ),
    ]