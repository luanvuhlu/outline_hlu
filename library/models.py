# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator
from account.models import Account, CreatorModel
from common.models import BaseModel, AddressModel, NameModel
from university.models import UClass, SpecializedStudy, Scholastic, Subject, Course, University

# Create your models here.
class Library(BaseModel, AddressModel, NameModel, CreatorModel):
    university=models.ForeignKey(University, blank=False, null=False)
    class Meta:
        verbose_name = u'Thư viện'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name_abbr if self.name_abbr else self.name

class LearningResourceType(BaseModel, CreatorModel):
    name=models.CharField(blank=False, max_length=100,
                          verbose_name=u'Tên loại')
    class Meta:
        verbose_name=u'Loại học liệu'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name
class Publishing(BaseModel, CreatorModel, NameModel):
    class Meta:
        verbose_name=u'Nhà xuất bản'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name
class LearningResource(BaseModel, CreatorModel):
    name=models.CharField(blank=False, max_length=255,
                          verbose_name=u'Tên')
    author=models.CharField(blank=True, max_length=255,
                            verbose_name=u'Tác giả')
    publishing=models.ForeignKey(Publishing, blank=True, null=True,
                                 verbose_name=u'Nhà xuất bản',
                                 help_text=u'Để trống nếu không có')
    pub_year=models.SmallIntegerField(blank=True,
                                      validators=[MaxValueValidator(datetime.now().year)],
                                      verbose_name=u'Năm xuất bản')
    library=models.ForeignKey(Library, blank=True, null=True,
                              verbose_name=u'Thư viện',
                              help_text=u'Để trống nếu không có')
    resource_type=models.ForeignKey(LearningResourceType, blank=True, null=True,
                                    verbose_name=u'Loại tài liệu',
                                    help_text=u'Để trống nếu không có')
    is_avaiable=models.BooleanField(blank=False, default=True, verbose_name=u'Có sẵn',
                                    help_text=u'Có ở thư viện hoặc được bày bán không')
    is_sale=models.BooleanField(blank=False, default=False, verbose_name=u'Có bán')
    sale_place=models.CharField(blank=True, max_length=255, verbose_name=u'Nơi bán',
                                help_text=u'Để trống nếu bán ngay tại trường')
    is_borrow=models.BooleanField(blank=False, default=True, verbose_name=u'Có thể mượn')
    borrow_place=models.CharField(blank=True, max_length=255, verbose_name=u'Nơi mượn',
                                  help_text=u'Để trống nếu cho mượn ngay tại thư viện')
    description = models.CharField(blank=True, max_length=255,
                                   verbose_name=u'Mô tả')
    class Meta:
        verbose_name = u'Học liệu'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name