# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date, datetime
import logging
from django.db import models
from homework.models import HomeWork
from account.models import CreatorModel
from common.models import BaseModel, DescriptionField
from outline.models import Outline
from university.models import University, Scholastic

logger = logging.getLogger(__name__)
# Create your models here.
WEEK_ORDER_CHOICES=[(order, order) for order in range(0, 16)]
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
        return u'Năm học %s Học kỳ %s Đợt %s' % (self.semester.scholastic.name, self.semester.order, self.order)
class Week(BaseModel, CreatorModel):
    outline=models.ForeignKey(Outline, blank=False,
                              verbose_name=u'Đề cương')
    order=models.SmallIntegerField(blank=False, choices=WEEK_ORDER_CHOICES,
                              verbose_name=u'Số thứ tự của tuần')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Tuần học'
        verbose_name_plural=verbose_name
    def university_name(self):
        return self.outline.subject.specialized_study.university
    university_name.short_description = u'Đại học'
    def __unicode__(self):
        return u'Tuần %s - %s' % (self.order, self.outline.__unicode__())
class SubjectSchedule(BaseModel, CreatorModel):
    week=models.ForeignKey(Week, blank=False)
    description = DescriptionField()
    class Meta:
        verbose_name=u'Lịch trình học hàng tuần'
        verbose_name_plural=verbose_name
    def university_name(self):
        return self.outline.subject.specialized_study.university
    university_name.short_description = u'Đại học'
    def __unicode__(self):
        return self.week.__unicode__()
class LearningDay(BaseModel, CreatorModel):
    week=models.ForeignKey(Week, blank=False, verbose_name=u'Tuần')
    TYPE_CHOICES=(
        (0, u'Lý thuyết'),
        (1, u'Thảo luận'),
        (2, u'Tự học'),
    )
    ORDER_CHOICES = [(x, x) for x in range(1, 3)]
    day_type=models.SmallIntegerField(blank=False, choices=TYPE_CHOICES,
                                  verbose_name=u'Giờ')
    order = models.SmallIntegerField(blank=True, null=True, choices=ORDER_CHOICES,
                                    help_text=u'Để trống nếu chỉ có 1 giờ',
                                     verbose_name=u'Số')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Ngày học'
        verbose_name_plural=verbose_name
    def university_name(self):
        return self.week.outline.subject.specialized_study.university
    university_name.short_description = u'Đại học'
    def outline_name(self):
        return self.week.outline
    outline_name.short_description = u'Đề cương'
    def __unicode__(self):
        return u'Giờ %s Tuần %s' % (self.get_day_type_display(), self.week)
class LearningDayContent(BaseModel, CreatorModel):
    day=models.ForeignKey(LearningDay, verbose_name=u'Ngày học')
    # ORDER_CHOICES = [(order, order) for order in range(1, 11)]
    # order = models.SmallIntegerField(blank=False, choices=ORDER_CHOICES,
    #                                  verbose_name=u'Thứ tự')
    content = models.CharField(blank=False, max_length=255,
                           verbose_name=u'Nội dung')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Nội dung học'
        verbose_name_plural = verbose_name
    def university_name(self):
        return self.day.week.outline.subject.specialized_study.university
    university_name.short_description = u'Đại học'
    def __unicode__(self):
        return u'Giờ %s Tuần %s' % (self.day.get_day_type_display(), self.day.week)
class LearningDayRequirement(BaseModel, CreatorModel):
    day = models.ForeignKey(LearningDay, verbose_name=u'Ngày học')
    # ORDER_CHOICES = [(order, order) for order in range(1, 11)]
    # order = models.SmallIntegerField(blank=False, choices=ORDER_CHOICES,
    #                                  verbose_name=u'Thứ tự')
    content = models.CharField(blank=False, max_length=255,
                               verbose_name=u'Yêu cầu')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Yêu cầu chuẩn bị cho giờ học'
        verbose_name_plural = verbose_name
    def university_name(self):
        return self.day.week.outline.subject.specialized_study.university
    university_name.short_description = u'Đại học'
    def __unicode__(self):
        return u'Giờ %s Tuần %s' % (self.day.get_day_type_display(), self.day.week)
class HomeWorkAction(BaseModel, CreatorModel):
    # TODO otutline in form and filter by it
    homework=models.ForeignKey(HomeWork, verbose_name=u'Bài tập')
    week=models.ForeignKey(Week, null=True, blank=True, verbose_name=u'Tuần')
    TYPE_CHOICES=(
        (0, u'Nhận'),
        (1, u'Nộp'),
        (2, u'Thuyết trình'),
        (3, u'Làm'),
    )
    hwa_type=models.SmallIntegerField(blank=False,
                                    default=0,
                                    choices = TYPE_CHOICES,
                                  verbose_name=u'Hoạt động')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Hoạt động bài tập'
        verbose_name_plural=verbose_name
    def university_name(self):
        return self.homework.outline.subject.specialized_study.university
    university_name.short_description = u'Đại học'
    def __unicode__(self):
        return '%s %s' % (self.get_hwa_type_display(), self.homework)
class CurrentWeek(BaseModel, CreatorModel):
    semester=models.ForeignKey(Semester, blank=False, verbose_name=u'Học kỳ')
    start_date=models.DateField(blank=False, null=False, verbose_name=u'Ngày bắt đầu')
    end_date=models.DateField(blank=False, null=False, verbose_name=u'Ngày kết thúc')
    description = DescriptionField()
    current_week_15 = models.SmallIntegerField(blank=False, default=0,
                                               choices = WEEK_ORDER_CHOICES,
                                               verbose_name = u'Tuần hiện tại môn 15 tuần')
    WEEK_5_ORDER_CHOICES=[(order, order) for order in range(0, 6)]
    current_week_5 = models.SmallIntegerField(blank=False, default=0,
                                               choices = WEEK_5_ORDER_CHOICES,
                                               verbose_name = u'Tuần hiện tại môn 5 tuần')
    off_next_week = models.BooleanField(blank=False, null=False, default=False,
                                verbose_name=u'Bỏ qua tuần sau', help_text=u'Tuần sau được nghỉ')
    class Meta:
        verbose_name=u'Tuần hiện tại'
        verbose_name_plural=verbose_name
    def university_name(self):
        return self.semester.university
    university_name.short_description = u'Đại học'
    def __unicode__(self):
        return u'Tuần hiện tại'