# -*- coding: utf-8 -*-
from django.contrib import admin
from common.admin import BaseAdmin
from models import HomeWorkFormat, HomeWork
# Register your models here.
@admin.register(HomeWorkFormat)
class HomeWorkFormatAdmin(BaseAdmin):
    pass
@admin.register(HomeWork)
class HomeWorkAdmin(BaseAdmin):
    list_display = ('type_order_name', 'outline', 'create_time')
    list_display_links = ('type_order_name', )
    fieldsets =(
        (None, {'fields': ('outline', ('type', 'order'), ('page_limit_start', 'page_limit_end'))}),
        (u'Khác', {'fields': ('handwritten', 'is_presenstation_required', 'presentation', 'other_requirement')})
    )
