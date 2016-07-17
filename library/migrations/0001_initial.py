# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 08:32
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Th\u1eddi gian t\u1ea1o')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='Th\u1eddi gian c\u1eadp nh\u1eadt')),
                ('name', models.CharField(max_length=255, verbose_name='T\xean')),
                ('author', models.CharField(blank=True, max_length=255, verbose_name='T\xe1c gi\u1ea3')),
                ('pub_year', models.SmallIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(2016)], verbose_name='N\u0103m xu\u1ea5t b\u1ea3n')),
                ('is_avaiable', models.BooleanField(default=True, verbose_name='C\xf3 s\u1eb5n')),
                ('is_sale', models.BooleanField(default=False, verbose_name='C\xf3 b\xe1n')),
                ('sale_place', models.CharField(blank=True, max_length=255, verbose_name='N\u01a1i b\xe1n')),
                ('is_borrow', models.BooleanField(default=True, verbose_name='C\xf3 th\u1ec3 m\u01b0\u1ee3n')),
                ('borrow_place', models.CharField(blank=True, max_length=255, verbose_name='N\u01a1i m\u01b0\u1ee3n')),
                ('creator', models.ForeignKey(help_text='L\xe0 ng\u01b0\u1eddi d\xf9ng hi\u1ec7n t\u1ea1i', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ng\u01b0\u1eddi t\u1ea1o')),
            ],
            options={
                'verbose_name': 'H\u1ecdc li\u1ec7u',
                'verbose_name_plural': 'H\u1ecdc li\u1ec7u',
            },
        ),
        migrations.CreateModel(
            name='LearningResourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Th\u1eddi gian t\u1ea1o')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='Th\u1eddi gian c\u1eadp nh\u1eadt')),
                ('name', models.CharField(max_length=100, verbose_name='T\xean lo\u1ea1i')),
                ('creator', models.ForeignKey(help_text='L\xe0 ng\u01b0\u1eddi d\xf9ng hi\u1ec7n t\u1ea1i', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ng\u01b0\u1eddi t\u1ea1o')),
            ],
            options={
                'verbose_name': 'Lo\u1ea1i h\u1ecdc li\u1ec7u',
                'verbose_name_plural': 'Lo\u1ea1i h\u1ecdc li\u1ec7u',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='T\xean')),
                ('name_abbr', models.CharField(blank=True, max_length=255, verbose_name='T\xean vi\u1ebft t\u1eaft')),
                ('address_1', models.CharField(blank=True, max_length=100, verbose_name='\u0110\u1ecba ch\u1ec9 1')),
                ('address_2', models.CharField(blank=True, max_length=100, verbose_name='\u0110\u1ecba ch\u1ec9 2')),
                ('address_3', models.CharField(blank=True, max_length=100, verbose_name='\u0110\u1ecba ch\u1ec9 3')),
                ('city', models.SmallIntegerField(choices=[(0, 'An Giang'), (1, 'B\xe0 R\u1ecba - V\u0169ng T\xe0u'), (2, 'B\u1ea1c Li\xeau'), (3, 'B\u1eafc Giang'), (4, 'B\u1eafc K\u1ea1n'), (5, 'B\u1eafc Ninh'), (6, 'B\u1ebfn Tre'), (7, 'B\xecnh D\u01b0\u01a1ng'), (8, 'B\xecnh \u0110\u1ecbnh'), (9, 'B\xecnh Ph\u01b0\u1edbc'), (10, 'B\xecnh Thu\u1eadn'), (11, 'C\xe0 Mau'), (12, 'Cao B\u1eb1ng'), (13, 'C\u1ea7n Th\u01a1'), (14, '\u0110\xe0 N\u1eb5ng'), (15, '\u0110\u1eafk L\u1eafk'), (16, '\u0110\u1eafk N\xf4ng'), (17, '\u0110i\u1ec7n Bi\xean'), (18, '\u0110\u1ed3ng Nai'), (19, '\u0110\u1ed3ng Th\xe1p'), (20, 'Gia Lai'), (21, 'H\xe0 Giang'), (22, 'H\xe0 Nam'), (23, 'H\xe0 N\u1ed9i'), (24, 'H\xe0 T\u0129nh'), (25, 'H\u1ea3i D\u01b0\u01a1ng'), (26, 'H\u1ea3i Ph\xf2ng'), (27, 'H\u1eadu Giang'), (28, 'H\xf2a B\xecnh'), (29, 'H\u01b0ng Y\xean'), (30, 'Kh\xe1nh H\xf2a'), (31, 'Ki\xean Giang'), (32, 'Kon Tum'), (33, 'Lai Ch\xe2u'), (34, 'L\u1ea1ng S\u01a1n'), (35, 'L\xe0o Cai'), (36, 'L\xe2m \u0110\u1ed3ng'), (37, 'Long An'), (38, 'Nam \u0110\u1ecbnh'), (39, 'Ngh\u1ec7 An'), (40, 'Ninh B\xecnh'), (41, 'Ninh Thu\u1eadn'), (42, 'Ph\xfa Th\u1ecd'), (43, 'Ph\xfa Y\xean'), (44, 'Qu\u1ea3ng B\xecnh'), (45, 'Qu\u1ea3ng Nam'), (46, 'Qu\u1ea3ng Ng\xe3i'), (47, 'Qu\u1ea3ng Ninh'), (48, 'Qu\u1ea3ng Tr\u1ecb'), (49, 'S\xf3c Tr\u0103ng'), (50, 'S\u01a1n La'), (51, 'T\xe2y Ninh'), (52, 'Th\xe1i B\xecnh'), (53, 'Th\xe1i Nguy\xean'), (54, 'Thanh H\xf3a'), (55, 'Th\u1eeba Thi\xean Hu\u1ebf'), (56, 'Ti\u1ec1n Giang'), (57, 'TP HCM'), (58, 'Tr\xe0 Vinh'), (59, 'Tuy\xean Quang'), (60, 'V\u0129nh Long'), (61, 'V\u0129nh Ph\xfac'), (62, 'Y\xean B\xe1i')], null=True, verbose_name='Th\xe0nh ph\u1ed1')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Th\u1eddi gian t\u1ea1o')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='Th\u1eddi gian c\u1eadp nh\u1eadt')),
                ('creator', models.ForeignKey(help_text='L\xe0 ng\u01b0\u1eddi d\xf9ng hi\u1ec7n t\u1ea1i', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ng\u01b0\u1eddi t\u1ea1o')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University')),
            ],
            options={
                'verbose_name': 'Th\u01b0 vi\u1ec7n',
                'verbose_name_plural': 'Th\u01b0 vi\u1ec7n',
            },
        ),
        migrations.AddField(
            model_name='learningresource',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Library'),
        ),
        migrations.AddField(
            model_name='learningresource',
            name='resource_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.LearningResourceType'),
        ),
    ]
