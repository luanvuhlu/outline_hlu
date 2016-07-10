# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

# class NameModel(models.Model):
#     name=models.CharField(blank=True)
#     name_abbr=models.CharField(blank=False)
#     class Meta:
#         abstract = True
# class AddressModel(models.Model):
#     address_1=models.CharField(blank=False)
#     address_2=models.CharField(blank=False)
#     address_3=models.CharField(blank=False)
#     city=models.CharField(blank=True)
#     class Meta:
#         abstract = True
class HistoryModel(models.Model):
    create_time=models.DateTimeField(auto_now_add=True, blank=False, verbose_name=u'Thời gian tạo')
    update_time=models.DateTimeField(blank=True, verbose_name=u'Thời gian cập nhật')
    # TODO
    class Meta:
        abstract = True
# class CreatorModel(models.Model):
#     user=models.ForeignKey('account.models.User', blank=True)
#     class Meta:
#         abstract = True