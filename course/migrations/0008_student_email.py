# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-21 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_teacher_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='', max_length=20, unique=True, verbose_name='邮箱'),
            preserve_default=False,
        ),
    ]
