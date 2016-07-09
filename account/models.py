from __future__ import unicode_literals

from django.conf.global_settings import EMAIL_BACKEND
from django.db import models
from django.contrib.auth.models import User
from common.models import HistoryModel

class Role(models.Model):
    name=models.CharField(max_length=30, verbose_name=u'Tên', help_text=u'Tên Role')
    # TODO
    # ALL=0
    # VIEW=1
    # UPDATE=2
    # DELETE=3
    # VALUE_CHOICES = (
    #     (ALL, 'Full'),
    #     (VIEW, u'Xem'),
    #     (UPDATE, u'Sửa'),
    #     (UPDATE, u'Xóa'),
    # )
    # value=models.SmallIntegerField(choices=VALUE_CHOICES,
    #                                default=ALL,
    #                                verbose_name='')
    description=models.CharField(max_length=200, blank=True)
    def __unicode__(self):
        return self.name
class Account(HistoryModel):
    EMAIL_PASS=0
    GOOGLE = 1
    FACEBOOK = 2
    LOGIN_TYPE_CHOICES=(
        (EMAIL_PASS, u'Email - Mật khẩu'),
        (GOOGLE, u'Google'),
        (FACEBOOK, u'Facebook'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creator=models.ForeignKey(u'self', null=False, editable=False,
                              verbose_name=u'Người tạo',
                              help_text=u'Là người dùng hiện tại')
    login_type=models.SmallIntegerField(blank=False,
                                        choices=LOGIN_TYPE_CHOICES,
                                        default=EMAIL_PASS,
                                        verbose_name=u'Kiểu đăng nhập',
                                        help_text=u'Kiểu đăng nhập'
                                        )
    reset_pass_key=models.CharField(blank=True, null=True, max_length=255,
                                    verbose_name=u'Key đặt lại mật khẩu',
                                    help_text=u'Được tạo tự động')
    reset_pass_expire=models.DateTimeField(blank=True, null=True)
    action_yn=models.BooleanField(blank=True, default=True)
    delete_yn=models.BooleanField(blank=True, default=False)
    block_yn=models.BooleanField(blank=True, default=False)
    block_expire=models.DateTimeField(blank=False)
    avarta_url_full=models.CharField(blank=True)
    avarta_url=models.CharField(blank=True)
    failure_count=models.IntegerField(blank=True, default=0)
    login_again_yn=models.BooleanField(blank=True, default=False)
    date_of_birth=models.DateField(blank=True)
    role=models.ForeignKey(Role, blank=True)
    family_name=models.CharField(blank=True)
    name=models.CharField(blank=True)
    description=models.CharField(blank=False)
    address_1 = models.CharField(blank=False)
    address_2 = models.CharField(blank=False)
    address_3 = models.CharField(blank=False)
    city = models.CharField(blank=True)

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