# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import Account, CreatorModel
from common.models import BaseModel, DescriptionField
from outline.models import Outline

# Create your models here.
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
    description = DescriptionField()
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
    ORDER_CHOICES=[(x, x) for x in range(0, 3)]
    order=models.SmallIntegerField(blank=False,
                                   default=0,
                                   choices=ORDER_CHOICES,
                                   verbose_name=u'Thứ tự',
                                   help_text=u'Chọn 0 nếu chỉ có 1 bài tập')
    format=models.ForeignKey(HomeWorkFormat, verbose_name=u'Định dạng')
    page_limit_start=models.SmallIntegerField(blank=True,
                                              null=True,
                                              verbose_name=u'Số trang tối thiểu',
                                              help_text=u'Để trống nếu không bắt buộc')
    page_limit_end = models.SmallIntegerField(blank=True,
                                              null=True,
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
    description = DescriptionField()
    class Meta:
        verbose_name=u'Bài tập'
        verbose_name_plural=verbose_name
    def type_order_name(self):
        if self.order:
            return "%s %s" % (self.get_type_display(), self.order)
        return self.get_type_display()

    type_order_name.short_description = u'Tên'
    def __unicode__(self):
        if self.order:
            return "%s %s %s" % (self.get_type_display(), self.order, self.outline.__unicode__())
        return "%s %s" % (self.get_type_display(), self.outline.__unicode__())