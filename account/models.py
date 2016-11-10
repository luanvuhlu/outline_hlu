# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.global_settings import EMAIL_BACKEND
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from softdelete.models import SoftDeleteObject, SoftDeleteManager
from common.models import BaseModel, AddressModel, DescriptionField

class AccountManager(BaseUserManager, SoftDeleteManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(u'Người dùng phải có email')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError(u'Người dùng phải có email')
        user = self.model(email=self.normalize_email(email))
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
    # REQUIRED_FIELDS = ('family_name', 'name', )
    objects = AccountManager()
    email = models.EmailField(
        max_length=255,
        unique=True,
        error_messages={
            'unique': u'Địa chỉ email đã tồn tại',
        },
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
    family_name=models.CharField(blank=False, max_length=255,
                                 verbose_name=u'Họ',
                                 help_text=u'Họ và tên đệm')
    name=models.CharField(blank=False, max_length=255,
                          verbose_name=u'Tên')
    description = DescriptionField()
    def get_full_name(self):
        return self.email
    def username(self):
        return self.email
    def get_short_name(self):
        return self.email
    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    def __unicode__(self):
        return self.email
    @staticmethod
    def autocomplete_search_fields():
        return ("email__icontains", "name__icontains", )
class CreatorModel(models.Model):
    creator = models.ForeignKey(Account,
                                blank=False,
                                null=False,
                                # editable=False,
                                verbose_name=u'Người tạo')
    class Meta:
        abstract = True
        