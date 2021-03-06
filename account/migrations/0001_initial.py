# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-15 04:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('address_1', models.CharField(blank=True, max_length=100, verbose_name='\u0110\u1ecba ch\u1ec9 1')),
                ('address_2', models.CharField(blank=True, max_length=100, verbose_name='\u0110\u1ecba ch\u1ec9 2')),
                ('address_3', models.CharField(blank=True, max_length=100, verbose_name='\u0110\u1ecba ch\u1ec9 3')),
                ('city', models.SmallIntegerField(choices=[(0, 'An Giang'), (1, 'B\xe0 R\u1ecba - V\u0169ng T\xe0u'), (2, 'B\u1ea1c Li\xeau'), (3, 'B\u1eafc Giang'), (4, 'B\u1eafc K\u1ea1n'), (5, 'B\u1eafc Ninh'), (6, 'B\u1ebfn Tre'), (7, 'B\xecnh D\u01b0\u01a1ng'), (8, 'B\xecnh \u0110\u1ecbnh'), (9, 'B\xecnh Ph\u01b0\u1edbc'), (10, 'B\xecnh Thu\u1eadn'), (11, 'C\xe0 Mau'), (12, 'Cao B\u1eb1ng'), (13, 'C\u1ea7n Th\u01a1'), (14, '\u0110\xe0 N\u1eb5ng'), (15, '\u0110\u1eafk L\u1eafk'), (16, '\u0110\u1eafk N\xf4ng'), (17, '\u0110i\u1ec7n Bi\xean'), (18, '\u0110\u1ed3ng Nai'), (19, '\u0110\u1ed3ng Th\xe1p'), (20, 'Gia Lai'), (21, 'H\xe0 Giang'), (22, 'H\xe0 Nam'), (23, 'H\xe0 N\u1ed9i'), (24, 'H\xe0 T\u0129nh'), (25, 'H\u1ea3i D\u01b0\u01a1ng'), (26, 'H\u1ea3i Ph\xf2ng'), (27, 'H\u1eadu Giang'), (28, 'H\xf2a B\xecnh'), (29, 'H\u01b0ng Y\xean'), (30, 'Kh\xe1nh H\xf2a'), (31, 'Ki\xean Giang'), (32, 'Kon Tum'), (33, 'Lai Ch\xe2u'), (34, 'L\u1ea1ng S\u01a1n'), (35, 'L\xe0o Cai'), (36, 'L\xe2m \u0110\u1ed3ng'), (37, 'Long An'), (38, 'Nam \u0110\u1ecbnh'), (39, 'Ngh\u1ec7 An'), (40, 'Ninh B\xecnh'), (41, 'Ninh Thu\u1eadn'), (42, 'Ph\xfa Th\u1ecd'), (43, 'Ph\xfa Y\xean'), (44, 'Qu\u1ea3ng B\xecnh'), (45, 'Qu\u1ea3ng Nam'), (46, 'Qu\u1ea3ng Ng\xe3i'), (47, 'Qu\u1ea3ng Ninh'), (48, 'Qu\u1ea3ng Tr\u1ecb'), (49, 'S\xf3c Tr\u0103ng'), (50, 'S\u01a1n La'), (51, 'T\xe2y Ninh'), (52, 'Th\xe1i B\xecnh'), (53, 'Th\xe1i Nguy\xean'), (54, 'Thanh H\xf3a'), (55, 'Th\u1eeba Thi\xean Hu\u1ebf'), (56, 'Ti\u1ec1n Giang'), (57, 'TP HCM'), (58, 'Tr\xe0 Vinh'), (59, 'Tuy\xean Quang'), (60, 'V\u0129nh Long'), (61, 'V\u0129nh Ph\xfac'), (62, 'Y\xean B\xe1i')], null=True, verbose_name='Th\xe0nh ph\u1ed1')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Th\u1eddi gian t\u1ea1o')),
                ('update_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Th\u1eddi gian c\u1eadp nh\u1eadt')),
                ('email', models.EmailField(error_messages={'unique': '\u0110\u1ecba ch\u1ec9 email \u0111\xe3 t\u1ed3n t\u1ea1i'}, max_length=255, unique=True)),
                ('login_type', models.SmallIntegerField(choices=[(0, 'Email - M\u1eadt kh\u1ea9u'), (1, 'Google'), (2, 'Facebook')], default=0, help_text='Ki\u1ec3u \u0111\u0103ng nh\u1eadp', verbose_name='Ki\u1ec3u \u0111\u0103ng nh\u1eadp')),
                ('reset_pass_key', models.CharField(blank=True, help_text='\u0110\u01b0\u1ee3c t\u1ea1o t\u1ef1 \u0111\u1ed9ng khi ng\u01b0\u1eddi d\xf9ng \u0111\u1eb7t l\u1ea1i m\u1eadt kh\u1ea9u', max_length=255, null=True, verbose_name='Key \u0111\u1eb7t l\u1ea1i m\u1eadt kh\u1ea9u')),
                ('reset_pass_expire', models.DateTimeField(blank=True, help_text='\u0110\u01b0\u1ee3c t\u1ea1o t\u1ef1 \u0111\u1ed9ng khi ng\u01b0\u1eddi d\xf9ng \u0111\u1eb7t l\u1ea1i m\u1eadt kh\u1ea9u', null=True, verbose_name='H\u1ea1n \u0111\u1eb7t l\u1ea1i m\u1eadt kh\u1ea9u')),
                ('is_admin', models.BooleanField(default=False, help_text='\u0110\u1eb7t l\xe0 ng\u01b0\u1eddi qu\u1ea3n tr\u1ecb', verbose_name='Qu\u1ea3n tr\u1ecb')),
                ('is_active', models.BooleanField(default=True, help_text='Tr\u1ea1ng th\xe1i ho\u1ea1t \u0111\u1ed9ng hi\u1ec7n t\u1ea1i c\u1ee7a t\xe0i kho\u1ea3n', verbose_name='\u0110ang ho\u1ea1t \u0111\u1ed9ng')),
                ('is_block', models.BooleanField(default=False, help_text='T\xe0i kho\u1ea3n c\xf3 \u0111ang b\u1ecb kho\xe1 kh\xf4ng', verbose_name='Kho\xe1')),
                ('block_expire', models.DateTimeField(blank=True, help_text='H\u1ea1n kho\xe1 t\xe0i kho\u1ea3n. \u0110\u1ec3 tr\u1ed1ng \u0111\u1ec3 kh\xf3a v\xf4 th\u1eddi h\u1ea1n', null=True, verbose_name='H\u1ea1n kho\xe1 t\xe0i kho\u1ea3n')),
                ('avarta_url_full', models.URLField(blank=True, help_text='\u0110\u01b0\u1eddng d\u1eabn \u1ea3nh \u0111\u1ea1i di\u1ec7n. \u0110\u1ec3 tr\u1ed1ng \u0111\u1ec3 d\xf9ng \u1ea3nh m\u1eb7c \u0111\u1ecbnh', max_length=255, verbose_name='\u0110\u01b0\u1eddng d\u1eabn \u1ea3nh \u0111\u1ea1i di\u1ec7n')),
                ('avarta_url', models.URLField(blank=True, help_text='\u0110\u01b0\u1eddng d\u1eabn \u1ea3nh \u0111\u1ea1i di\u1ec7n thu nh\u1ecf. \u0110\u1ec3 tr\u1ed1ng \u0111\u1ec3 d\xf9ng \u1ea3nh m\u1eb7c \u0111\u1ecbnh', verbose_name='\u0110\u01b0\u1eddng d\u1eabn \u1ea3nh \u0111\u1ea1i di\u1ec7n thu nh\u1ecf')),
                ('failure_count', models.SmallIntegerField(default=0, help_text='S\u1ed1 l\u1ea7n \u0111\u0103ng nh\u1eadp l\u1ed7i. N\u1ebfu v\u01b0\u1ee3t qu\xe1 s\u1ed1 l\u1ea7n, s\u1ebd b\u1ecb kh\xf3a t\xe0i kho\u1ea3n', verbose_name='S\u1ed1 l\u1ea7n \u0111\u0103ng nh\u1eadp l\u1ed7i')),
                ('is_login_again_required', models.BooleanField(default=False, help_text='Y\xeau c\u1ea7u ng\u01b0\u1eddi d\xf9ng ph\u1ea3i \u0111\u0103ng nh\u1eadp l\u1ea1i.', verbose_name='Y\xeau c\u1ea7u ph\u1ea3i \u0111\u0103ng nh\u1eadp l\u1ea1i')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Ng\xe0y sinh')),
                ('family_name', models.CharField(help_text='H\u1ecd v\xe0 t\xean \u0111\u1ec7m', max_length=255, verbose_name='H\u1ecd')),
                ('name', models.CharField(max_length=255, verbose_name='T\xean')),
                ('creator', models.ForeignKey(help_text='L\xe0 ng\u01b0\u1eddi d\xf9ng hi\u1ec7n t\u1ea1i', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ng\u01b0\u1eddi t\u1ea1o')),
            ],
            options={
                'verbose_name': 'T\xe0i kho\u1ea3n',
                'verbose_name_plural': 'T\xe0i kho\u1ea3n',
            },
        ),
    ]
