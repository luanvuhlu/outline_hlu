# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import Account, CreatorModel
from common.models import BaseModel
from university.models import UClass, SpecializedStudy, Scholastic, Subject, Course
from library.models import LearningResource

# Create your models here.
class Outline(BaseModel, CreatorModel):
    scholastic=models.ForeignKey(Scholastic, blank=False, null=False,
                                 verbose_name=u'Năm học')
    subject=models.ForeignKey(Subject, blank=False, null=False,
                              verbose_name=u'Môn học')
    course=models.ForeignKey(Course, blank=False, null=False,
                             verbose_name=u'Khóa')
    description=models.CharField(blank=True, max_length=255,
                                 verbose_name=u'Mô tả')
    class Meta:
        verbose_name=u'Đề cương'
        verbose_name_plural=verbose_name
class OutlineLearningResource(BaseModel, CreatorModel):
    REQUIRED_TYPE=0
    OPTION_TYPE=1
    RESOURCE_TYPE_CHOICES=(
        (REQUIRED_TYPE, u'Bắt buộc'),
        (OPTION_TYPE, u'Tham khảo'),
    )
    outline=models.ForeignKey(Outline, blank=False, null=False,
                              verbose_name=u'Đề cương')
    learning_resource=models.ForeignKey(LearningResource, blank=False, null=False,
                                        verbose_name=u'Học liệu')
    resource_type=models.SmallIntegerField(blank=False,
                                   choices=RESOURCE_TYPE_CHOICES,
                                   verbose_name=u'Loại tài liệu')
    class Meta:
        verbose_name = u'Tài liệu cho môn học'
        verbose_name_plural = verbose_name
class Problem(BaseModel, CreatorModel):
    name=models.CharField(blank=False, max_length=255,
                          verbose_name=u'Tên vấn đề')
    description = models.CharField(blank=True, max_length=255,
                                   verbose_name=u'Mô tả')
    class Meta:
        verbose_name = u'Vấn đề'
        verbose_name_plural = verbose_name
class ProblemDetail(BaseModel, CreatorModel):
    problem=models.ForeignKey(Problem, blank=False, null=False,
                              verbose_name=u'Vấn đề')
    content=models.CharField(blank=True, max_length=255,
                             verbose_name=u'Nội dung vấn đề')
    description = models.CharField(blank=True, max_length=255,
                                   verbose_name=u'Mô tả')

    class Meta:
        verbose_name = u'Nội dung vấn đề'
        verbose_name_plural = verbose_name

class Week(BaseModel, CreatorModel):
    ORDER_CHOICES=[(order, order) for order in range(1, 15)]
    outline=models.ForeignKey(Outline, blank=False,
                              verbose_name=u'Đề cương')
    order=models.SmallIntegerField(blank=False, choices=ORDER_CHOICES,
                              verbose_name=u'Số thứ tự của tuần')
    description = models.CharField(blank=True, max_length=255,
                                   verbose_name=u'Mô tả')
    class Meta:
        verbose_name=u'Tuần học'
        verbose_name_plural=verbose_name
class SubjectSchedule(BaseModel, CreatorModel):
    outline=models.ForeignKey(Outline, blank=False,
                              verbose_name=u'Đề cương')
    week=models.ForeignKey(Week, blank=False)
    class Meta:
        verbose_name=u'Lịch trình học'
        verbose_name_plural=verbose_name
