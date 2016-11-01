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
class Faculty(BaseModel, NameModel, CreatorModel):
    address = models.CharField(blank=True, max_length=100,
                                 verbose_name=u'Địa chỉ')
    university=models.ForeignKey(University, blank=False, verbose_name=u'Trường đại học')
    description = DescriptionField()
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
    address = models.CharField(blank=True, max_length=100,
                                 verbose_name=u'Địa chỉ')
    university=models.ForeignKey(University, blank=False, verbose_name=u'Trường đại học')
    description = DescriptionField()
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
    description = DescriptionField()
    class Meta:
        verbose_name=u'Khoá'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name_abbr if self.name_abbr else self.name
class UClass(BaseModel, NameModel, CreatorModel):
    course=models.ForeignKey(Course, verbose_name=u'Khoá')
    # TODO department
    description = DescriptionField()
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
    CREDIT_CHOICES = [(i, "%s tín chỉ" % i) for i in range(1, 6)]
    specialized_study=models.ForeignKey(SpecializedStudy, blank=True, verbose_name=u'Bộ môn')
    credit=models.SmallIntegerField(blank=False, default=2,
                               choices=CREDIT_CHOICES,
                               verbose_name=u'Số tín chỉ')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Môn học'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name
    def get_university(self):
        return self.specialized_study.university
    get_university.short_description=u'Đại học'
    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains", "name_abbr__icontains")
class Person(BaseModel, CreatorModel):
    nick_name = models.CharField(blank=True, max_length=255,
                                 verbose_name=u'Biệt hiệu')
    description = DescriptionField()
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
    account = models.ForeignKey(Account, verbose_name=u'Tài khoản', related_name='student_account')
    u_class=models.ForeignKey(UClass, verbose_name=u'Lớp')
    class Meta:
        verbose_name = u'Sinh viên'
        verbose_name_plural = verbose_name
class Lecturer(Person):
    account = models.ForeignKey(Account, verbose_name=u'Tài khoản', related_name='lecture_account')
    # TODO department
class Scholastic(BaseModel, CreatorModel):
    name = models.CharField(blank=False, max_length=255,
                            verbose_name=u'Tên')
    start_date=models.DateField(blank=False, null=False, verbose_name=u'Ngày bắt đầu')
    end_date=models.DateField(blank=False, null=False, verbose_name=u'Ngày kết thúc')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Năm học'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name
class Semester(BaseModel, CreatorModel):
    university=models.ForeignKey(University, blank=False, null=False, verbose_name=u'Trường đại học')
    scholastic=models.ForeignKey(Scholastic, blank=False, null=False,
                                 verbose_name=u'Năm học')
    ORDER_CHOICES = [(order, u'Kỳ %s' % order) for order in range(1, 3)]
    order = models.SmallIntegerField(blank=False, null=True, choices=ORDER_CHOICES,
                                    default=1,
                                    verbose_name=u'Học kỳ')
    start_date=models.DateField(blank=True, null=False, verbose_name=u'Ngày bắt đầu',
                                    help_text=u'Để trống nếu trùng với ngày của năm học')
    end_date=models.DateField(blank=True, null=False, verbose_name=u'Ngày kết thúc',
                                    help_text=u'Để trống nếu trùng với ngày của năm học')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Học kỳ'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'Năm học %s Học kỳ %s' % (self.scholastic.name, self.order)
class StudySession(BaseModel, CreatorModel):
    semester=models.ForeignKey(Semester, blank=False, null=False,
                                 verbose_name=u'Học kỳ')
    ORDER_CHOICES = (
        (None, None),
        (0, u'15 tuần'),
        (1, 1),
        (2, 2),
        (3, 3),)
    order = models.SmallIntegerField(blank=False, null=False, choices=ORDER_CHOICES,
                                    default=None,
                                    verbose_name=u'Đợt',
                                    help_text=u'Để 0 nếu là môn 15 tuần')
    start_date=models.DateField(blank=True, null=False, verbose_name=u'Ngày bắt đầu',
                                    help_text=u'Để trống nếu trùng với ngày của kỳ học')
    end_date=models.DateField(blank=True, null=False, verbose_name=u'Ngày kết thúc',
                                    help_text=u'Để trống nếu trùng với ngày của kỳ học')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Đợt học'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        if self.order == 0 :
            return u'Năm học %s Học kỳ %s' % (self.semester.scholastic.name, self.semester.order)        
        return u'Năm học %s Học kỳ %s Đợt %s' % (self.semester.scholastic.name, self.semester.order, self.order)