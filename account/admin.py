# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from common.admin import BaseAdmin
from models import Account

@admin.register(Account)
class UserAdmin(BaseUserAdmin, BaseAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    radio_fields = {'login_type': admin.VERTICAL}
    list_display = ('email', 'date_of_birth', 'is_admin', 'deleted')
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        (u'Thông tin người dùng', {'fields': (
            ('family_name', 'name'),
            'date_of_birth',
            'address_1',
            'address_2',
            'address_3',
            'city',
            'avarta_url_full',
            'avarta_url',
        )}),
        (u'Trạng thái hoạt động', {'fields': (
            'is_active',
            'is_block',
            'block_expire',
        )}),
        (u'Quyền hạn', {'fields': ('is_admin',)}),
        (u'Khác', {'fields': ('description', )}),
        (u'Lịch sử', {'fields': ('creator', 'create_time', 'update_time',)}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('Wide', ),
            'fields' : ('email',
                        'password1',
                        'password2',)
        }),
        (u'Thông tin người dùng', {'fields': (
            ('family_name', 'name'),
            'date_of_birth',
            'address_1',
            'address_2',
            'address_3',
            'city',
        )}),
        (u'Quyền hạn', {'fields': ('is_admin',)}),
        (u'Khác', {'fields': ('description', )}),
    )
    search_fields = ('email', )
    ordering = ('email', )
    filter_horizontal = ()
    list_filter = ('is_admin',)
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return self.fieldsets+BaseAdmin.fieldsets
    def get_readonly_fields(self, request, obj=None):
        self.readonly_fields = self.readonly_fields + ('creator', 'create_time', 'update_time')
        if not obj:  # Add Mode
            exclude_fields=('creator', 'create_time', 'update_time')
            return tuple(field for field in self.readonly_fields if field not in exclude_fields)
        return self.readonly_fields+('email', )

        # if obj: #Changing Mode
        #     # Readonly Email
        #     return self.readonly_fields+('email',)
        # return self.readonly_fields
