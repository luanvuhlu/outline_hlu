# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils import timezone
from common.admin import BaseAdmin
from common.models import BaseModel
from account.models import CreatorModel
from models import Week, Scholastic, SubjectSchedule, LearningDay, LearningDayContent, LearningDayRequirement, HomeWorkAction, CurrentWeek, StudySession, Semester
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
class StudySessionInline(admin.TabularInline):
    model = StudySession
    exclude = ('description', 'creator', 'create_time', 'deleted_at', 'update_time')
    extra = 4
    #TODO add start_date and end_date
@admin.register(Scholastic)
class ScholasticAdmin(BaseAdmin):
    list_display = ('name', 'start_date', 'end_date', 'create_time')
    readonly_fields = ('name', )
    fieldsets = (
        (None, {'fields': ('name', 'start_date', 'end_date')}),
    )
    def save_model(self, request, obj, form, change):
        obj.name = '%s-%s' % (obj.start_date.year, obj.end_date.year)
        BaseAdmin.save_model(self, request, obj, form, change)
    class Meta:
        model = Scholastic
@admin.register(Semester)
class SemesterAdmin(BaseAdmin):
    inlines = [StudySessionInline]
    list_display = ('order', 'scholastic', 'start_date', 'end_date', 'university', 'create_time')
    fieldsets = (
        (None, {'fields': ('university', 'scholastic', 'order', ('start_date', 'end_date'))}),
    )
    radio_fields = {'order': admin.HORIZONTAL}
    class Meta:
        model = Semester
    def save_model(self, request, obj, form, change):
        if not obj.start_date:
            obj.start_date = obj.scholastic.start_date
        if not obj.end_date:
            obj.end_date = obj.scholastic.end_date
        BaseAdmin.save_model(self, request, obj, form, change)
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if not instance.start_date:
                instance.start_date = instance.semester.start_date
            if not instance.end_date:
                instance.end_date = instance.semester.end_date
            if isinstance(instance, BaseModel):
                instance.update_time = timezone.now()
            if isinstance(instance, CreatorModel) and not instance.creator_id:
                instance.creator = request.user
            instance.save()
@admin.register(StudySession)
class StudySessionAdmin(BaseAdmin):
    list_display = ('semester', 'order', 'start_date', 'end_date', 'create_time')
    fieldsets = (
        (None, {'fields': ('semester', 'order', ('start_date', 'end_date'))}),
    )
    radio_fields = {'order': admin.HORIZONTAL}
    def save_model(self, request, obj, form, change):
        if not obj.start_date:
            obj.start_date = obj.semester.start_date
        if not obj.end_date:
            obj.end_date = obj.semester.end_date
        BaseAdmin.save_model(self, request, obj, form, change)
    class Meta:
        model = StudySession
@admin.register(CurrentWeek)
class CurrentWeekAdmin(BaseAdmin):
    list_display = ('university', 'current_week_15', 'current_week_5', 'start_date', 'end_date', 'create_time')
    fieldsets = (
        (None, {'fields': ('university', ('start_date', 'end_date'), 'current_week_15', 'current_week_5')}),
    )

    # readonly_fields = ('start_date', 'end_date')
# @admin.register(LearningDayContent)
# class LearningDayContentAdmin(BaseAdmin):
#     pass
# @admin.register(LearningDayRequirement)
# class LearningDayRequirementAdmin(BaseAdmin):
#     pass
# @admin.register(HomeWorkAction)
# class HomeWorkActionAdmin(BaseAdmin):
#     pass
