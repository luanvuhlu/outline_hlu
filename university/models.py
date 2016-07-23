# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import Account, CreatorModel
from common.models import BaseModel, CITIES_CHOICES, AddressModel, NameModel, DescriptionField

# Create your models here.
class University(BaseModel, AddressModel, NameModel, CreatorModel):
    founding=models.DateField(blank=False, verbose_name=u'Ngày thành lập')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Đại học'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name_abbr if self.name_abbr else self.name

class SpecializedStudy(BaseModel, NameModel, CreatorModel):
    address = models.CharField(blank=True, max_length=100,
                                 verbose_name=u'Địa chỉ')
    university=models.ForeignKey(University, blank=False, verbose_name=u'Trường đại học')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Khoa'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name_abbr if self.name_abbr else self.name

class Course(BaseModel, NameModel, CreatorModel):
    university=models.ForeignKey(University, blank=False, verbose_name=u'Trường đại học')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Khoá'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name_abbr if self.name_abbr else self.name
class UClass(BaseModel, NameModel, CreatorModel):
    course=models.ForeignKey(Course, verbose_name=u'Khoá')
    specialized_study=models.ForeignKey(SpecializedStudy, verbose_name=u'Bộ môn/Khoa')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Lớp'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name_abbr if self.name_abbr else self.name
class Subject(BaseModel, NameModel, CreatorModel):
    CREDIT_CHOICES = [(i, i) for i in range(1, 6)]
    specialized_study=models.ForeignKey(SpecializedStudy, blank=True, verbose_name=u'Bộ môn/Khoa')
    credit=models.SmallIntegerField(blank=False, default=2,
                               choices=CREDIT_CHOICES,
                               verbose_name=u'Số tín chỉ')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Môn học'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name_abbr if self.name_abbr else self.name

class Scholastic(BaseModel, CreatorModel):
    name = models.CharField(blank=False, max_length=255,
                            verbose_name=u'Tên')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Năm học'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
class Student(BaseModel, CreatorModel):
    account = models.ForeignKey(Account, verbose_name=u'Tài khoản', related_name='student_account')
    nick_name=models.CharField(blank=True, max_length=255,
                            verbose_name=u'Biệt hiệu')
    u_class=models.ForeignKey(UClass, verbose_name=u'Lớp')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Sinh viên'
        verbose_name_plural = verbose_name
class Lecturer(BaseModel, CreatorModel):
    account=models.ForeignKey(Account, verbose_name=u'Tài khoản', related_name='lecture_account')
    nick_name=models.CharField(blank=True, max_length=255,
                            verbose_name=u'Biệt hiệu')
    specialized_study=models.ForeignKey(SpecializedStudy, blank=False)
    description = DescriptionField()
    class Meta:
        verbose_name = u'Giảng viên'
        verbose_name_plural = verbose_name