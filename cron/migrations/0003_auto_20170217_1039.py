# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-17 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cron', '0002_auto_20161214_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronjob',
            name='command',
            field=models.CharField(help_text='Posix shell command which will be executed', max_length=1024, verbose_name='Command'),
        ),
    ]
