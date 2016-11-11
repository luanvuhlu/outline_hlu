# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import Account, CreatorModel
from common.models import BaseModel, DescriptionField
from university.models import UClass, Subject, Course, StudySession
from library.models import LearningResource

DAY_OF_WEEK_CHOICE=(
        (0, u'Thứ 2'),
        (1, u'Thứ 3'),
        (2, u'Thứ 4'),
        (3, u'Thứ 5'),
        (4, u'Thứ 6'),
        (5, u'Thứ 7'),
        (6, u'Chủ nhật'),
    )
# Create your models here.
class Outline(BaseModel, CreatorModel):
    study_session=models.ForeignKey(StudySession, blank=False, null=False,
                                 verbose_name=u'Đợt học')
    subject=models.ForeignKey(Subject, blank=False, null=False,
                              verbose_name=u'Môn học')
    course=models.ForeignKey(Course, blank=True, null=True,
                             verbose_name=u'Khóa')
    STUDY_TIME_TYPE=(
        (0, u'15 tuần'),
        (1, u'5 tuần'),
    )
    study_time_type=models.SmallIntegerField(blank=False, default=0, null=False,
                                choices=STUDY_TIME_TYPE,
                                verbose_name=u'Tuần học')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Đề cương'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return '%s %s' % (self.subject, self.study_session)
    def course_verbose(self):
        return self.course if self.course else u'Tất cả'
    course_verbose.short_description = u'Khoá'
    def university_verbose(self):
        return self.subject.specialized_study.university
    university_verbose.short_description = u'Đại học'
    @staticmethod
    def autocomplete_search_fields():
        return ("subject__name__icontains", "course__name")
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
    resource_type=models.SmallIntegerField(blank=False, default=REQUIRED_TYPE,
                                   choices=RESOURCE_TYPE_CHOICES,
                                   verbose_name=u'Loại tài liệu')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Tài liệu cho môn học'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.learning_resource.__unicode__()
class Problem(BaseModel, CreatorModel):
    outline=models.ForeignKey(Outline, blank=False, null=False,
                              verbose_name=u'Đề cương')
    name=models.CharField(blank=False, max_length=255,
                          verbose_name=u'Tên vấn đề')
    ORDER_CHOICES=[(x, x) for x in range(1, 16)]
    order=models.SmallIntegerField(blank=False, choices=ORDER_CHOICES,
                                   verbose_name=u'Số')
    description = DescriptionField()
    class Meta:
        verbose_name = u'Vấn đề'
        verbose_name_plural = verbose_name
    def university_name(self):
        return self.outline.subject.specialized_study.university
    university_name.short_description = u'Đại học'
    def __unicode__(self):
        return 'Vấn đề %s' % self.order
class ProblemDetail(BaseModel, CreatorModel):
    problem=models.ForeignKey(Problem, blank=False, null=False,
                              verbose_name=u'Vấn đề')
    content=models.CharField(blank=False, max_length=255,
                             verbose_name=u'Nội dung vấn đề')
    ORDER_CHOICES = [(x, x) for x in range(1, 11)]
    order = models.SmallIntegerField(blank=False, choices=ORDER_CHOICES,
                                     verbose_name=u'Số')
    description = DescriptionField()
    def outline_name(self):
        return self.problem.outline
    outline_name.short_description = u'Đề cương'
    def university_name(self):
        return self.problem.outline.subject.specialized_study.university
    university_name.short_description = u'Đại học'
    class Meta:
        verbose_name = u'Nội dung vấn đề'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return '%s.%s' % (self.problem.__unicode__(), self.order)
class TargetAwareness(BaseModel, CreatorModel):
    # TODO otutline in form and filter by it
    problem_detail=models.ForeignKey(ProblemDetail, blank=True, null=True,
                                     verbose_name=u'Vấn đề chi tiết')
    problem=models.ForeignKey(Problem, blank=True, null=True,
                              verbose_name=u'Vấn đề')
    LEVEL_CHOICES=[(x, x) for x in range(1, 4)]
    level=models.SmallIntegerField(blank=False, choices=LEVEL_CHOICES,
                                   verbose_name=u'Bậc')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Mục tiêu nhận thức'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return '%s - Bậc %s' % (self.problem_detail.__unicode__(), self.level)
class TargetAwarenessDetail(BaseModel, CreatorModel):
    target_awareness=models.ForeignKey(TargetAwareness, verbose_name=u'Mức tiêu nhận thức')
    ORDER_CHOICES =[(x, x) for x in range(1, 11)]
    order=models.SmallIntegerField(blank=False,
                                         verbose_name=u'Thứ tự')
    content=models.TextField(blank=False, max_length=500,
                             verbose_name=u'Nội dung')
    description = DescriptionField()
class AdvisoryTime(BaseModel, CreatorModel):
    outline=models.ForeignKey(Outline, blank=False, verbose_name=u'Đề cương')
    day_of_week=models.SmallIntegerField(blank=False, choices=DAY_OF_WEEK_CHOICE,
                                         verbose_name=u'Ngày')
    start_time=models.TimeField(blank=True, verbose_name=u'Bắt đầu')
    end_time = models.TimeField(blank=True, verbose_name=u'Kết thúc')
    place=models.CharField(blank=True, max_length=255,
                           verbose_name=u'Địa điểm')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Thời gian tư vấn'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return '%s %s' % (self.outline.__unicode__(), self.get_day_of_week_display())
