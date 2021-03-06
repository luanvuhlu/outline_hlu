# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-15 04:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import homework.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Th\u1eddi gian t\u1ea1o')),
                ('update_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Th\u1eddi gian c\u1eadp nh\u1eadt')),
                ('hw_type', models.SmallIntegerField(choices=[(0, 'C\xe1 nh\xe2n'), (1, 'C\xe1 nh\xe2n ki\u1ec3m tra'), (2, 'Nh\xf3m th\xe1ng'), (3, 'H\u1ecdc k\u1ef3')], default=0, verbose_name='Lo\u1ea1i b\xe0i t\u1eadp')),
                ('order', models.SmallIntegerField(choices=[(0, 0), (1, 1), (2, 2)], default=0, help_text='Ch\u1ecdn 0 n\u1ebfu ch\u1ec9 c\xf3 1 b\xe0i t\u1eadp', verbose_name='Th\u1ee9 t\u1ef1')),
                ('page_limit_start', models.SmallIntegerField(blank=True, help_text='\u0110\u1ec3 tr\u1ed1ng n\u1ebfu kh\xf4ng b\u1eaft bu\u1ed9c', null=True, verbose_name='S\u1ed1 trang t\u1ed1i thi\u1ec3u')),
                ('page_limit_end', models.SmallIntegerField(blank=True, help_text='\u0110\u1ec3 tr\u1ed1ng n\u1ebfu kh\xf4ng b\u1eaft bu\u1ed9c', null=True, verbose_name='S\u1ed1 trang t\u1ed1i \u0111a')),
                ('handwritten', models.BooleanField(default=False, verbose_name='Y\xeau c\u1ea7u vi\u1ebft tay')),
                ('is_not_presenstation_required', models.BooleanField(default=False, verbose_name='Kh\xf4ng y\xeau c\u1ea7u thuy\u1ebft tr\xecnh')),
                ('presentation', models.CharField(blank=True, max_length=255, verbose_name='N\u1ed9i dung thuy\u1ebft tr\xecnh')),
                ('other_requirement', models.CharField(blank=True, max_length=255, verbose_name='Y\xeau c\u1ea7u kh\xe1c')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ng\u01b0\u1eddi t\u1ea1o')),
            ],
            options={
                'verbose_name': 'B\xe0i t\u1eadp',
                'verbose_name_plural': 'B\xe0i t\u1eadp',
            },
        ),
        migrations.CreateModel(
            name='HomeWorkFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Th\u1eddi gian t\u1ea1o')),
                ('update_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Th\u1eddi gian c\u1eadp nh\u1eadt')),
                ('name', models.CharField(max_length=100, verbose_name='T\xean')),
                ('page_size', models.SmallIntegerField(blank=True, choices=[(0, 'A4')], default=0, help_text='Tu\u1ef3 ch\u1ecdn th\xec \u0111\u1ec3 tr\u1ed1ng', verbose_name='Kh\u1ed5 gi\u1ea5y')),
                ('font', models.SmallIntegerField(blank=True, choices=[(0, 'Times New Roman')], default=0, help_text='Tu\u1ef3 ch\u1ecdn th\xec \u0111\u1ec3 tr\u1ed1ng', verbose_name='Font ch\u1eef')),
                ('size_unit', models.SmallIntegerField(blank=True, choices=[(0, 'cm'), (1, 'inc')], default=0, verbose_name='\u0110\u01a1n vi \u0111o \u0111\u1ed9 d\xe0i')),
                ('top_margin', models.FloatField(blank=True, default=2.5, verbose_name='L\u1ec1 tr\xean')),
                ('bottom_margin', models.FloatField(blank=True, default=2.5, verbose_name='L\u1ec1 d\u01b0\u1edbi')),
                ('left_margin', models.FloatField(blank=True, default=3.5, verbose_name='L\u1ec1 tr\xe1i')),
                ('right_margin', models.FloatField(blank=True, default=2.0, verbose_name='L\u1ec1 ph\u1ea3i')),
                ('break_lines', models.FloatField(blank=True, default=1.5, verbose_name='D\xe3n d\xf2ng')),
                ('other', models.CharField(blank=True, max_length=255, verbose_name='Y\xeau c\u1ea7u kh\xe1c')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ng\u01b0\u1eddi t\u1ea1o')),
            ],
            options={
                'verbose_name': '\u0110\u1ecbnh d\u1ea1ng b\xe0i t\u1eadp',
                'verbose_name_plural': '\u0110\u1ecbnh d\u1ea1ng b\xe0i t\u1eadp',
            },
        ),
        migrations.CreateModel(
            name='HomeWorkQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Th\u1eddi gian t\u1ea1o')),
                ('update_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Th\u1eddi gian c\u1eadp nh\u1eadt')),
                ('no', models.CharField(blank=True, help_text='S\u1ed1 th\u1ee9 t\u1ef1 \u0111\u1ec1. \u0110\u1ec3 0 n\u1ebfu kh\xf4ng x\xe1c \u0111\u1ecbnh. <br />N\u1ebfu \u0111\u1ec1 b\xe0i thay \u0111\u1ed5i theo l\u1edbp, vui l\xf2ng ghi t\xean l\u1edbp v\xe0o', max_length=50, verbose_name='\u0110\u1ec1')),
                ('content', models.CharField(blank=True, max_length=500, verbose_name='N\u1ed9i dung')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ng\u01b0\u1eddi t\u1ea1o')),
                ('home_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.HomeWork', verbose_name='B\xe0i t\u1eadp')),
            ],
            options={
                'verbose_name': '\u0110\u1ec1 b\xe0i t\u1eadp',
                'verbose_name_plural': '\u0110\u1ec1 b\xe0i t\u1eadp',
            },
        ),
        migrations.CreateModel(
            name='HomeWorkQuestionAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Th\u1eddi gian t\u1ea1o')),
                ('update_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Th\u1eddi gian c\u1eadp nh\u1eadt')),
                ('document', models.FileField(max_length=200, upload_to='questions/%Y/%m/%d/', validators=[homework.validators.validate_homework_file_extension], verbose_name='HomeWork Question')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ng\u01b0\u1eddi t\u1ea1o')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.HomeWorkQuestion', verbose_name='\u0110\u1ec1 b\xe0i')),
            ],
            options={
                'verbose_name': 'File \u0111\xednh k\xe8m \u0111\u1ec1 b\xe0i t\u1eadp',
                'verbose_name_plural': 'File \u0111\xednh k\xe8m \u0111\u1ec1 b\xe0i t\u1eadp',
            },
        ),
        migrations.CreateModel(
            name='HomeWorkSolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Th\u1eddi gian t\u1ea1o')),
                ('update_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Th\u1eddi gian c\u1eadp nh\u1eadt')),
                ('solution_type', models.SmallIntegerField(choices=[(0, 'L\u1eddi gi\u1ea3i'), (1, 'G\u1ee3i \xfd'), (2, 'D\xe0n b\xe0i')], default=0, verbose_name='Lo\u1ea1i')),
                ('content', models.CharField(blank=True, help_text='Vui l\xf2ng t\u1ea3i l\xean file n\u1ebfu n\u1ed9i dung qu\xe1 d\xe0i', max_length=500, verbose_name='N\u1ed9i dung')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ng\u01b0\u1eddi t\u1ea1o')),
                ('home_work_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.HomeWorkQuestion', verbose_name='Gi\u1ea3i ph\xe1p')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomeWorkSolutionAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Th\u1eddi gian t\u1ea1o')),
                ('update_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Th\u1eddi gian c\u1eadp nh\u1eadt')),
                ('document', models.FileField(max_length=200, upload_to='solutions/%Y/%m/%d/', validators=[homework.validators.validate_homework_file_extension], verbose_name='HomeWork Solution')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ng\u01b0\u1eddi t\u1ea1o')),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.HomeWorkQuestion', verbose_name='Gi\u1ea3i ph\xe1p')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='homework',
            name='hw_format',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.HomeWorkFormat', verbose_name='\u0110\u1ecbnh d\u1ea1ng'),
        ),
    ]
