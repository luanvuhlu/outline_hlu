# -*- coding: utf-8 -*-
from django.contrib import admin
from common.admin import BaseAdmin
from models import Library, LearningResource, LearningResourceType, Publishing
from django.forms.utils import flatatt
# Register your models here.

@admin.register(Library)
class LibraryAdmin(BaseAdmin):
    list_display = ('name', 'university', 'city', 'create_time')
    fieldsets = (
        (None, {'fields': ('name', 'name_abbr', 'university')}),
        (u'Địa chỉ', {'fields': ('address_1', 'address_2', 'address_3', 'city', )}),
    )
    class Meta:
        model = Library
@admin.register(Publishing)
class PublishingAdmin(BaseAdmin):
    list_display = ('name', 'create_time')
    fieldsets = (
        (None, {'fields': ('name', 'name_abbr', )}),
    )
    class Meta:
        model = Publishing
@admin.register(LearningResource)
class LearningResourceAdmin(BaseAdmin):
    list_display = ('name', 'resource_type', 'author', 'publishing','pub_year', 'create_time')
    fieldsets = (
        (None, {'fields' : (('name', 'resource_type'), 'author', ('publishing', 'pub_year'), 'library', 'is_avaiable')}),
        (u'Mượn', {'fields': (('is_borrow', 'borrow_place'), )}),
        (u'Bán', {'fields': (('is_sale', 'sale_place'), )}),
        (u'Khác', {'fields': ('description', )}),
    )
    class Meta:
        model = LearningResource
@admin.register(LearningResourceType)
class LearningResourceTypeAdmin(BaseAdmin):
    list_display = ('name', 'create_time')
    fieldsets = (
        (None, {'fields': ('name', )}),
    )
    class Meta:
        model = LearningResourceType