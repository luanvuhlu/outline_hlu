# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from common.admin import BaseAdmin
from models import Week, SubjectSchedule, LearningDay, LearningDayContent, LearningDayRequirement, HomeWorkAction
# Register your models here.
class HomeWorkActionInline(admin.TabularInline):
    model = HomeWorkAction
    exclude = ('description', 'creator', 'create_time', 'deleted_at', 'update_time')
    extra = 5
class LearningDayInline(admin.TabularInline):
    model = LearningDay
    radio_fields = {'day_type': admin.VERTICAL, 'order': admin.VERTICAL}
    exclude = ('description', 'creator', 'create_time', 'deleted_at', 'update_time')
    extra = 3
class WeekInline(admin.TabularInline):
    model = Week
    exclude = ('description', 'creator', 'create_time', 'deleted_at', 'update_time')
    extra = 16
@admin.register(Week)
class WeekAdmin(BaseAdmin):
    inlines = [HomeWorkActionInline]
    list_display = ('outline', 'order', 'university_name', 'create_time')
    fieldsets = (
        (None, {'fields': ('outline', 'order')}),
    )
    raw_id_fields =('outline', )
    autocomplete_lookup_fields = {
        'fk': ['outline'],
    }
    ordering = ('outline', 'order')
    search_fields = ['outline__subject__name', '=order', '^outline__scholastic__name', 'outline__course__university__name']
    list_filter = (
        ('order'),
    )
# @admin.register(SubjectSchedule)
# class SubjectScheduleAdmin(BaseAdmin):
#     pass
class LearningDayContentInline(admin.TabularInline):
    model = LearningDayContent
    exclude = ('description', 'creator', 'create_time', 'deleted_at', 'update_time')
    extra = 5
class LearningDayRequirementInline(admin.TabularInline):
    model = LearningDayRequirement
    exclude = ('description', 'creator', 'create_time', 'deleted_at', 'update_time')
    extra = 5
@admin.register(LearningDay)
class LearningDayAdmin(BaseAdmin):
    inlines = [LearningDayContentInline, LearningDayRequirementInline]
    list_display = ('outline_name', 'week', 'day_type', 'order', 'university_name', 'create_time')
    fieldsets = (
        (None, {'fields': ('week', 'day_type', 'order')}),
    )
    radio_fields = {'order' : admin.VERTICAL}
    # readonly_fields = ('outline_name', 'university_name', )
# @admin.register(LearningDayContent)
# class LearningDayContentAdmin(BaseAdmin):
#     pass
# @admin.register(LearningDayRequirement)
# class LearningDayRequirementAdmin(BaseAdmin):
#     pass
# @admin.register(HomeWorkAction)
# class HomeWorkActionAdmin(BaseAdmin):
#     pass
