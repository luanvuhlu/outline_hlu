# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-15 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('outline', '0001_initial'),
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='outline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outline.Outline', verbose_name='\u0110\u1ec1 c\u01b0\u01a1ng'),
        ),
    ]