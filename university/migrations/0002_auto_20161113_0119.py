# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-12 18:19
from __future__ import unicode_literals

import common.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='code',
            field=models.CharField(blank=True, max_length=25, verbose_name='M\xe3 sinh vi\xean'),
        ),
        migrations.AddField(
            model_name='subject',
            name='code',
            field=models.CharField(blank=True, max_length=25, verbose_name='M\xe3 m\xf4n h\u1ecdc'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='order',
            field=models.SmallIntegerField(choices=[(1, 'K\u1ef3 1'), (2, 'K\u1ef3 2'), (3, 'K\u1ef3 3')], default=1, null=True, verbose_name='H\u1ecdc k\u1ef3'),
        ),
    ]
