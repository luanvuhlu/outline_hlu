# -*- coding: utf-8 -*-
from django.contrib import admin
from common.admin import BaseAdmin
from models import HomeWorkFormat, HomeWork
# Register your models here.
@admin.register(HomeWorkFormat)
class HomeWorkFormatAdmin(BaseAdmin):
    list_display = ('name', 'create_time')
    list_display_links = ('name', )
    fieldsets =(
        (None, {'fields': ('name', ('font', 'page_size'), 'size_unit', ('top_margin', 'bottom_margin', 'left_margin', 'right_margin'), 'break_lines')}),
        (u'Yêu cầu khác', {'fields': ('other', )})
    )
@admin.register(HomeWork)
class HomeWorkAdmin(BaseAdmin):
    list_display = ('type_order_name', 'outline', 'create_time')
    list_display_links = ('type_order_name', )
    fieldsets =(
        (None, {'fields': ('outline', ('hw_type', 'order'), ('page_limit_start', 'page_limit_end'))}),
        (u'Yêu cầu khác', {'fields': ('handwritten', 'is_not_presenstation_required', 'presentation', 'other_requirement')})
    )
