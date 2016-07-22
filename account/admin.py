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
    readonly_fields = (
                       'reset_pass_key',
                       )
    radio_fields = {'login_type': admin.VERTICAL}
    list_display = ('email', 'date_of_birth', 'is_admin', 'deleted')
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        (u'Thông tin người dùng', {'fields': (
            'date_of_birth',
            ('family_name', 'name'),
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
    )
    add_fieldsets = (
        (None, {
            'classes' : ('Wide', ),
            'fields' : ('email',
                        'password1',
                        'password2',)
        }),
        (u'Thông tin người dùng', {'fields': (
            'date_of_birth',
            'family_name',
            'name',
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
        return self.fieldsets
    def get_readonly_fields(self, request, obj=None):
        if obj: #Changing Mode
            # Readonly Email
            return self.readonly_fields+('email',)
        return self.readonly_fields
