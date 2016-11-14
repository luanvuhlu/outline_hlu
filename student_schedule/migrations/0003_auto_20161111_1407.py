# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-11 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_schedule', '0002_auto_20161111_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningdaysubjectschedule',
            name='day_type',
            field=models.SmallIntegerField(choices=[(0, 'L\xfd thuy\u1ebft'), (1, 'Th\u1ea3o lu\u1eadn'), (2, 'T\u1ef1 h\u1ecdc')], default=1, verbose_name='Gi\u1edd'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='learningdaysubjectschedule',
            name='day_of_week',
            field=models.SmallIntegerField(choices=[(0, 'Th\u1ee9 2'), (1, 'Th\u1ee9 3'), (2, 'Th\u1ee9 4'), (3, 'Th\u1ee9 5'), (4, 'Th\u1ee9 6'), (5, 'Th\u1ee9 7'), (6, 'Ch\u1ee7 nh\u1eadt')], verbose_name='Ng\xe0y trong tu\u1ea7n'),
        ),
    ]
