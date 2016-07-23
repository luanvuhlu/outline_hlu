# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from homework.models import HomeWork

from account.models import CreatorModel
from common.models import BaseModel, DescriptionField
from outline.models import Outline
# Create your models here.
class Week(BaseModel, CreatorModel):
    ORDER_CHOICES=[(order, order) for order in range(0, 16)]
    outline=models.ForeignKey(Outline, blank=False,
                              verbose_name=u'Đề cương')
    order=models.SmallIntegerField(blank=False, choices=ORDER_CHOICES,
                              verbose_name=u'Số thứ tự của tuần')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Tuần học'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return u'Tuần %s - %s' % (self.order, self.outline.__unicode__())
class SubjectSchedule(BaseModel, CreatorModel):
    week=models.ForeignKey(Week, blank=False)
    description = DescriptionField()
    class Meta:
        verbose_name=u'Lịch trình học hàng tuần'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.week.__unicode__()
class LearningDay(BaseModel, CreatorModel):
    week=models.ForeignKey(Week, blank=False, verbose_name=u'Tuần')
    TYPE_CHOICES=(
        (0, u'Lý thuyết'),
        (1, u'Thảo luận'),
    )
    type=models.SmallIntegerField(blank=False, choices=TYPE_CHOICES,
                                  default=0,
                                  verbose_name=u'Giờ')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Ngày học'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return u'Giờ %s Tuần %s' % (self.get_type_display(), self.week)
class LearningDayContent(BaseModel, CreatorModel):
    day=models.ForeignKey(LearningDay, verbose_name=u'Ngày học')
    ORDER_CHOICES = [(order, order) for order in range(1, 11)]
    order = models.SmallIntegerField(blank=False, choices=ORDER_CHOICES,
                                     verbose_name=u'Thứ tự')
    content = models.CharField(blank=False, max_length=255,
                           verbose_name=u'Nội dung')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Nội dung học'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return u'Giờ %s Tuần %s Nội dung thứ %s' % (self.day.get_type_display(), self.day.week, self.order)
class LearningDayRequirement(BaseModel, CreatorModel):
    day = models.ForeignKey(LearningDay, verbose_name=u'Ngày học')
    ORDER_CHOICES = [(order, order) for order in range(1, 11)]
    order = models.SmallIntegerField(blank=False, choices=ORDER_CHOICES,
                                     verbose_name=u'Thứ tự')
    content = models.CharField(blank=False, max_length=255,
                               verbose_name=u'Yêu cầu')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Yêu cầu chuẩn bị cho giờ học'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'Giờ %s Tuần %s Yêu cầu thứ %s' % (self.day.get_type_display(), self.day.week, self.order)
class HomeWorkAction(BaseModel, CreatorModel):
    # TODO otutline in form and filter by it
    home_work=models.ForeignKey(HomeWork, verbose_name=u'Bài tập')
    subject_schedule=models.ForeignKey(SubjectSchedule, verbose_name=u'Tuần')
    TYPE_CHOICES=(
        (0, u'Nhận'),
        (1, u'Nộp'),
        (2, u'Thuyết trình'),
    )
    type=models.SmallIntegerField(blank=False,
                                  verbose_name=u'Hoạt động')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Hoạt động bài tập'
        verbose_name_plural=verbose_name