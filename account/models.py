# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.global_settings import EMAIL_BACKEND
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from softdelete.models import SoftDeleteObject, SoftDeleteManager
from common.models import BaseModel, AddressModel


# class Role(models.Model):
#     name=models.CharField(max_length=30, verbose_name=u'Tên', help_text=u'Tên Role')
#     # TODO
#     # ALL=0
#     # VIEW=1
#     # UPDATE=2
#     # DELETE=3
#     # VALUE_CHOICES = (
#     #     (ALL, 'Full'),
#     #     (VIEW, u'Xem'),
#     #     (UPDATE, u'Sửa'),
#     #     (UPDATE, u'Xóa'),
#     # )
#     # value=models.SmallIntegerField(choices=VALUE_CHOICES,
#     #                                default=ALL,
#     #                                verbose_name='')
#     description=models.CharField(max_length=200, blank=True, verbose_name=u'Mô tả')
#     def __unicode__(self):
#         return self.name
class AccountManager(BaseUserManager, SoftDeleteManager):
    def create_user(self, email, city, password=None):
        if not email:
            raise ValueError(u'Người dùng phải có email')
        user = self.model(email=self.normalize_email(email), city=city)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, city, password=None):
        if not email:
            raise ValueError(u'Người dùng phải có email')
        user = self.model(email=self.normalize_email(email), city=city)
        user.set_password(password)
        user.is_admin=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, BaseModel, AddressModel):
    class Meta:
        verbose_name = u'Tài khoản'
        verbose_name_plural = u'Tài khoản'
    EMAIL_PASS=0
    GOOGLE = 1
    FACEBOOK = 2
    LOGIN_TYPE_CHOICES=(
        (EMAIL_PASS, u'Email - Mật khẩu'),
        (GOOGLE, u'Google'),
        (FACEBOOK, u'Facebook'),
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('family_name', 'name', )
    objects = AccountManager()
    email = models.EmailField(
        # verbose_name='Email',
        max_length=255,
        unique=True,
    )
    creator=models.ForeignKey(u'self',
                              null=True,
                              verbose_name=u'Người tạo',
                              help_text=u'Là người dùng hiện tại')
    login_type=models.SmallIntegerField(blank=False,
                                        choices=LOGIN_TYPE_CHOICES,
                                        default=EMAIL_PASS,
                                        verbose_name=u'Kiểu đăng nhập',
                                        help_text=u'Kiểu đăng nhập'
                                        )
    reset_pass_key=models.CharField(blank=True, null=True,
                                    max_length=255,
                                    verbose_name=u'Key đặt lại mật khẩu',
                                    help_text=u'Được tạo tự động khi người dùng đặt lại mật khẩu')
    reset_pass_expire=models.DateTimeField(blank=True, null=True,
                                           verbose_name=u'Hạn đặt lại mật khẩu',
                                           help_text=u'Được tạo tự động khi người dùng đặt lại mật khẩu')
    is_admin = models.BooleanField(default=False, verbose_name=u'Quản trị', help_text=u'Đặt là người quản trị')
    is_active=models.BooleanField(blank=False, default=True,
                                  verbose_name=u'Đang hoạt động',
                                  help_text=u'Trạng thái hoạt động hiện tại của tài khoản')
    # is_delete=models.BooleanField(blank=False, default=False,
    #                               verbose_name=u'Đã xoá',
    #                               help_text=u'Bản ghi đã được xoá hay chưa')
    is_block=models.BooleanField(blank=False, default=False,
                                 verbose_name=u'Khoá',
                                 help_text=u'Tài khoản có đang bị khoá không')
    block_expire=models.DateTimeField(blank=True, null=True,
                                      verbose_name=u'Hạn khoá tài khoản',
                                      help_text=u'Hạn khoá tài khoản. Để trống để khóa vô thời hạn')
    avarta_url_full=models.URLField(blank=True,
                                    max_length=255,
                                    verbose_name=u'Đường dẫn ảnh đại diện',
                                    help_text=u'Đường dẫn ảnh đại diện. Để trống để dùng ảnh mặc định')
    avarta_url=models.URLField(blank=True,
                                    verbose_name=u'Đường dẫn ảnh đại diện thu nhỏ',
                                    help_text=u'Đường dẫn ảnh đại diện thu nhỏ. Để trống để dùng ảnh mặc định')
    failure_count=models.SmallIntegerField(blank=False, default=0,
                                           verbose_name=u'Số lần đăng nhập lỗi',
                                           help_text=u'Số lần đăng nhập lỗi. Nếu vượt quá số lần, sẽ bị khóa tài khoản')
    is_login_again_required=models.BooleanField(blank=False, default=False,
                                       verbose_name=u'Yêu cầu phải đăng nhập lại',
                                       help_text=u'Yêu cầu người dùng phải đăng nhập lại.')
    date_of_birth=models.DateField(blank=True,
                                   null=True,
                                   verbose_name=u'Ngày sinh')
    # role=models.ForeignKey(Role, blank=False, verbose_name=u'Vai trò')
    family_name=models.CharField(blank=False, max_length=255,
                                 verbose_name=u'Họ',
                                 help_text=u'Họ và tên đệm')
    name=models.CharField(blank=False, max_length=255,
                          verbose_name=u'Tên')
    description=models.CharField(blank=True, max_length=255,
                                 verbose_name=u'Mô tả')
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    def __unicode__(self):
        return self.email
# class Page(HistoryModel):
#     title=models.CharField(max_length=255, verbose_name=u'Tiêu đề', help_text=u'Tiêu đề trang web')
#     url=models.CharField(max_length=255)
#     creator = models.ForeignKey(u'self', blank=False, editable=False,
#                                 verbose_name=u'Người tạo',
#                                 help_text=u'Là người dùng hiện tại')
#     description=models.CharField(blank=False)
# class Permission(HistoryModel):
#     page=models.ForeignKey(Page, blank=True)
#     role=models.ForeignKey(Role, blank=False)
#     permission=models.IntegerField(blank=True, default=0) #TODO
#     description=models.CharField(blank=False)
#     creator = models.ForeignKey(u'self', blank=False, editable=False,
#                                 verbose_name=u'Người tạo',
#                                 help_text=u'Là người dùng hiện tại')

class CreatorModel(models.Model):
    creator = models.ForeignKey(Account,
                                blank=False,
                                null=False,
                                verbose_name=u'Người tạo',
                                help_text=u'Là người dùng hiện tại')
    class Meta:
        abstract = True