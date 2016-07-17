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
    def __unicode__(self):
        return '%s %s' % (self.subject, self.course)
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
    description = models.CharField(blank=True, max_length=255,
                                   verbose_name=u'Mô tả')
    class Meta:
        verbose_name = u'Vấn đề'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return 'Vấn đề %s' % self.order
class ProblemDetail(BaseModel, CreatorModel):
    problem=models.ForeignKey(Problem, blank=False, null=False,
                              verbose_name=u'Vấn đề')
    content=models.CharField(blank=True, max_length=255,
                             verbose_name=u'Nội dung vấn đề')
    ORDER_CHOICES = [(x, x) for x in range(1, 10)]
    order = models.SmallIntegerField(blank=False, choices=ORDER_CHOICES,
                                     verbose_name=u'Số')
    description = models.CharField(blank=True, max_length=255,
                                   verbose_name=u'Mô tả')

    class Meta:
        verbose_name = u'Nội dung vấn đề'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return '%s.%s' % (self.problem.__unicode__(), self.order)
class Week(BaseModel, CreatorModel):
    ORDER_CHOICES=[(order, order) for order in range(0, 15)]
    outline=models.ForeignKey(Outline, blank=False,
                              verbose_name=u'Đề cương')
    order=models.SmallIntegerField(blank=False, choices=ORDER_CHOICES,
                              verbose_name=u'Số thứ tự của tuần')
    description = models.CharField(blank=True, max_length=255,
                                   verbose_name=u'Mô tả')
    class Meta:
        verbose_name=u'Tuần học'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return u'Tuần %s' % self.order
class HomeWorkFormat(BaseModel, CreatorModel):
    name=models.CharField(blank=False, max_length=100,
                          verbose_name=u'Tên')
    PAGE_SIZE_CHOICES = (
        (0, 'A4'),
    )
    page_size=models.SmallIntegerField(blank=True,
                          choices=PAGE_SIZE_CHOICES,
                                       default=0,
                          verbose_name=u'Khổ giấy',
                                  help_text=u'Tuỳ chọn thì để trống')
    FONT_CHOICES=(
        (0, 'Times New Roman'),
    )
    font=models.SmallIntegerField(blank=True,
                                  choices=FONT_CHOICES,
                                  default=0,
                                  verbose_name=u'Font chữ',
                                  help_text=u'Tuỳ chọn thì để trống')
    SIZE_UNIT_CHOICES=(
        (0, 'cm'),
        (1, 'inc'),
    )
    size_unit=models.SmallIntegerField(blank=True, choices=SIZE_UNIT_CHOICES, default=0,
                                       verbose_name=u'Đơn vi đo độ dài')
    top_margin = models.FloatField(blank=True, default=2.5,
                                   verbose_name=u'Lề trên')
    bottom_margin = models.FloatField(blank=True, default=2.5,
                                      verbose_name=u'Lề dưới')
    left_margin = models.FloatField(blank=True, default=3.5,
                                    verbose_name=u'Lề trái')
    right_margin = models.FloatField(blank=True, default=2.0,
                                    verbose_name=u'Lề phải')
    break_lines = models.FloatField(blank=True, default=1.5,
                                    verbose_name=u'Dãn dòng')
    other=models.CharField(blank=True, max_length=255,
                           verbose_name=u'Yêu cầu khác')
    description=models.CharField(blank=True, max_length=255,
                                 verbose_name=u'mô tả')
    class Meta:
        verbose_name=u'Định dạng bài tập'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name
class HomeWork(BaseModel, CreatorModel):
    outline=models.ForeignKey(Outline, verbose_name=u'Đề cương')
    TYPE_CHOICES=(
        (0, u'Cá nhân'),
        (1, u'Cá nhân kiểm tra'),
        (2, u'Nhóm tháng'),
        (3, u'Học kỳ'),
    )
    type=models.SmallIntegerField(blank=False, default=0,
                                  choices=TYPE_CHOICES,
                                  verbose_name=u'Loại bài tập')
    ORDER_CHOICES=[(x, x) for x in range(0, 2)]
    order=models.SmallIntegerField(blank=False, default=0,
                                   choices=ORDER_CHOICES,
                                   verbose_name=u'Thứ tự',
                                   help_text=u'Chọn 0 nếu chỉ có 1 bài tập')
    format=models.ForeignKey(HomeWorkFormat, verbose_name=u'Định dạng')
    page_limit_start=models.SmallIntegerField(blank=True,
                                              verbose_name=u'Số trang tối thiểu',
                                              help_text=u'Để trống nếu không bắt buộc')
    page_limit_end = models.SmallIntegerField(blank=True,
                                                verbose_name=u'Số trang tối đa',
                                                help_text=u'Để trống nếu không bắt buộc')
    handwritten=models.BooleanField(blank=False, null=False,
                                    default=False,
                                    verbose_name=u'Yêu cầu viết tay')
    is_presenstation_required=models.BooleanField(blank=False, null=False,
                                                  default=True,
                                                  verbose_name=u'Yêu cầu thuyết trình')
    presentation=models.CharField(blank=True, max_length=255,
                                  verbose_name=u'Nội dung thuyết trình')
    other_requirement=models.CharField(blank=True, max_length=255,
                                       verbose_name=u'Yêu cầu khác')
    class Meta:
        verbose_name=u'Bài tập'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return "%s %s" % (self.get_type_display(), self.order) if self.order else self.get_type_display()
class SubjectSchedule(BaseModel, CreatorModel):
    outline=models.ForeignKey(Outline, blank=False,
                              verbose_name=u'Đề cương')
    week=models.ForeignKey(Week, blank=False)
    class Meta:
        verbose_name=u'Lịch trình học hàng tuần'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.week.__unicode__()
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
    desciption=models.CharField(blank=True, max_length=255,
                                verbose_name=u'Mô tả')
    class Meta:
        verbose_name=u'Bài tập'
        verbose_name_plural=verbose_name
class TargetAwareness(BaseModel, CreatorModel):
    # TODO otutline in form and filter by it
    problem_detail=models.ForeignKey(ProblemDetail, blank=True, null=True,
                                     verbose_name=u'Vấn đề chi tiết')
    problem=models.ForeignKey(Problem, blank=True, null=True,
                              verbose_name=u'Vấn đề')
    LEVEL_CHOICES=[(x, x) for x in range(1, 4)]
    level=models.SmallIntegerField(blank=False, choices=LEVEL_CHOICES,
                                   verbose_name=u'Bậc')
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