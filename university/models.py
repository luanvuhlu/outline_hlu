# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import Account, CreatorModel
from common.models import BaseModel, AddressModel, NameModel

# Create your models here.
class University(BaseModel, AddressModel, NameModel, CreatorModel):
    founding=models.DateField(blank=True, 
                              null=True,
                              verbose_name=u'Ngày thành lập')
    class Meta:
        verbose_name=u'Đại học'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name_abbr if self.name_abbr else self.name
class Faculty(BaseModel, NameModel, CreatorModel):
    address = models.CharField(blank=True, max_length=100,
                                 verbose_name=u'Địa chỉ')
    university=models.ForeignKey(University, 
                                 blank=False, 
                                 verbose_name=u'Trường đại học')
    
    class Meta:
        verbose_name = u'Khoa'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name
    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains", )
class SpecializedStudy(BaseModel, NameModel, CreatorModel):
    faculty = models.ForeignKey(Faculty, blank=True, verbose_name=u'Khoa')
    address = models.CharField(blank=True, 
                               max_length=100,
                               verbose_name=u'Địa chỉ')
    university=models.ForeignKey(University, blank=False, verbose_name=u'Trường đại học')
    
    class Meta:
        verbose_name = u'Bộ môn'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name
    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains", )
class Course(BaseModel, NameModel, CreatorModel):
    university=models.ForeignKey(University, blank=False, verbose_name=u'Trường đại học')
    
    class Meta:
        verbose_name=u'Khoá'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name_abbr if self.name_abbr else self.name
class UClass(BaseModel, NameModel, CreatorModel):
    course=models.ForeignKey(Course, verbose_name=u'Khoá')
    # TODO department
    
    class Meta:
        verbose_name = u'Lớp'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name_abbr if self.name_abbr else self.name
    def full_name(self):
        return '%s%s' % (self.course, self.name)
    full_name.short_description = u'Tên'
    def get_university(self):
        return self.course.university
    get_university.short_description=u'Đại học'
    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains", )
class Subject(BaseModel, NameModel, CreatorModel):
    code = models.CharField(max_length=25,
                            blank=True,
                            verbose_name=u'Mã môn học')
    CREDIT_CHOICES = [(i, "%s tín chỉ" % i) for i in range(1, 6)]
    specialized_study=models.ForeignKey(SpecializedStudy, blank=True, verbose_name=u'Bộ môn')
    credit=models.SmallIntegerField(blank=False, default=2,
                               choices=CREDIT_CHOICES,
                               verbose_name=u'Số tín chỉ')
    
    class Meta:
        verbose_name=u'Môn học'
        verbose_name_plural=verbose_name
    def get_university(self):
        return self.specialized_study.university
    get_university.short_description=u'Đại học'
    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains", "name_abbr__icontains")
    def __unicode__(self):
        if self.code:
            return u'%s - %s' % (self.code, self.name)
        return self.name
class Person(BaseModel, CreatorModel):
    nick_name = models.CharField(blank=True, max_length=255,
                                 verbose_name=u'Biệt hiệu')
    
    class Meta:
        verbose_name = u'Giảng viên'
        verbose_name_plural = verbose_name
        abstract = True

    def get_family_name(self):
        return self.account.family_name

    def get_name(self):
        return self.account.name

    def get_email(self):
        return self.account.email
    def __unicode__(self):
        return self.account.__unicode__()
    get_email.short_description = 'Email'
    get_family_name.short_description = u'Họ'
    get_name.short_description = u'Tên'
class Student(Person):
    code = models.CharField(max_length=25,
                            blank=True,
                            verbose_name=u'Mã sinh viên')
    account = models.ForeignKey(Account, verbose_name=u'Tài khoản', related_name='student_account')
    u_class=models.ForeignKey(UClass, verbose_name=u'Lớp')
    class Meta:
        verbose_name = u'Sinh viên'
        verbose_name_plural = verbose_name
class Lecturer(Person):
    account = models.ForeignKey(Account, verbose_name=u'Tài khoản', related_name='lecture_account')
    # TODO department
class LessionTime(BaseModel, CreatorModel):
    university = models.ForeignKey(University,
                                blank=False,
                                null=False,
                                verbose_name=u'Đại học')
    name = models.CharField(max_length=10,
                            blank=True,
                            verbose_name=u'Tiết học')
    ORDER_CHOICES = [(order, order) for order in range(1, 15)]
    start = models.TimeField(blank=False, null=False, verbose_name=u'Bắt đầu')
    end = models.TimeField(blank=False, 
                            null=False, 
                            verbose_name=u'kết thúc',
                            help_text=u'Thời gian kết thúc phải nhỏ hơn thời gian bắt đầu')
    order = models.SmallIntegerField(blank=False,
                                    null=False, choices=ORDER_CHOICES,
                                    verbose_name=u'Thứ tự')
    
    class Meta:
        verbose_name = u'Tiết học'
        verbose_name_plural = verbose_name
    @staticmethod
    def autocomplete_search_fields():
        return ("university__name__icontains", "university__name_abbr__icontains", "name__icontains") 
    def __unicode__(self):
        return u'%s Tiết %s' %(self.university, self.name)