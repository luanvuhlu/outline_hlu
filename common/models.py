# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.query import QuerySet
from softdelete.models import SoftDeleteObject, SoftDeleteManager

# Create your models here.
CITIES_CHOICES = (
    (0, u'An Giang'),
    (1, u'Bà Rịa - Vũng Tàu'),
    (2, u'Bạc Liêu'),
    (3, u'Bắc Giang'),
    (4, u'Bắc Kạn'),
    (5, u'Bắc Ninh'),
    (6, u'Bến Tre'),
    (7, u'Bình Dương'),
    (8, u'Bình Định'),
    (9, u'Bình Phước'),
    (10, u'Bình Thuận'),
    (11, u'Cà Mau'),
    (12, u'Cao Bằng'),
    (13, u'Cần Thơ'),
    (14, u'Đà Nẵng'),
    (15, u'Đắk Lắk'),
    (16, u'Đắk Nông'),
    (17, u'Điện Biên'),
    (18, u'Đồng Nai'),
    (19, u'Đồng Tháp'),
    (20, u'Gia Lai'),
    (21, u'Hà Giang'),
    (22, u'Hà Nam'),
    (23, u'Hà Nội'),
    (24, u'Hà Tĩnh'),
    (25, u'Hải Dương'),
    (26, u'Hải Phòng'),
    (27, u'Hậu Giang'),
    (28, u'Hòa Bình'),
    (29, u'Hưng Yên'),
    (30, u'Khánh Hòa'),
    (31, u'Kiên Giang'),
    (32, u'Kon Tum'),
    (33, u'Lai Châu'),
    (34, u'Lạng Sơn'),
    (35, u'Lào Cai'),
    (36, u'Lâm Đồng'),
    (37, u'Long An'),
    (38, u'Nam Định'),
    (39, u'Nghệ An'),
    (40, u'Ninh Bình'),
    (41, u'Ninh Thuận'),
    (42, u'Phú Thọ'),
    (43, u'Phú Yên'),
    (44, u'Quảng Bình'),
    (45, u'Quảng Nam'),
    (46, u'Quảng Ngãi'),
    (47, u'Quảng Ninh'),
    (48, u'Quảng Trị'),
    (49, u'Sóc Trăng'),
    (50, u'Sơn La'),
    (51, u'Tây Ninh'),
    (52, u'Thái Bình'),
    (53, u'Thái Nguyên'),
    (54, u'Thanh Hóa'),
    (55, u'Thừa Thiên Huế'),
    (56, u'Tiền Giang'),
    (57, u'TP HCM'),
    (58, u'Trà Vinh'),
    (59, u'Tuyên Quang'),
    (60, u'Vĩnh Long'),
    (61, u'Vĩnh Phúc'),
    (62, u'Yên Bái'),
)
class NameModel(models.Model):
    name = models.CharField(blank=False, max_length=255,
                            verbose_name=u'Tên')

    name_abbr = models.CharField(blank=True, max_length=255,
                             verbose_name=u'Tên viết tắt')
    class Meta:
        abstract = True
class AddressModel(models.Model):
    address_1 = models.CharField(blank=True, max_length=100,
                                 verbose_name=u'Địa chỉ 1')
    address_2 = models.CharField(blank=True, max_length=100,
                                 verbose_name=u'Địa chỉ 2')
    address_3 = models.CharField(blank=True, max_length=100,
                                 verbose_name=u'Địa chỉ 3')
    city = models.SmallIntegerField(blank=False,
                                    null=True,
                                    choices=CITIES_CHOICES,
                                    verbose_name=u'Thành phố')
    class Meta:
        abstract = True
class BaseModel(SoftDeleteObject):
    objects = SoftDeleteManager()
    # deleted_at = models.DateTimeField(blank=True, null=True, default=None, verbose_name=u'Đã xoá lúc')
    create_time=models.DateTimeField(auto_now_add=True, blank=False, verbose_name=u'Thời gian tạo')
    update_time=models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=u'Thời gian cập nhật')
    class Meta:
        abstract = True