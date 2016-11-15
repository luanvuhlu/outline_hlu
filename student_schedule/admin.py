# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from common.admin import BaseAdmin
from models import StudentSchedule, SubjectStudentSchedule, LearningDaySubjectSchedule
# Register your models here.

class SubjectStudentScheduleAdminInline(admin.TabularInline):
    model = SubjectStudentSchedule
    exclude = ('creator', 'create_time', 'deleted_at', 'update_time')
    # radio_fields = {'study_session': admin.VERTICAL}
    raw_id_fields =('subject', 'outline')
    autocomplete_lookup_fields = {
        'fk': ['subject', 'outline'],
    }
    extra = 10
@admin.register(StudentSchedule)
class StudentScheduleAdmin(BaseAdmin):
    inlines = [SubjectStudentScheduleAdminInline]
    list_display = ('student', 'semester')
    fieldsets = (
        (None, {'fields': ('student', 'semester')}),
    )
class LearningDaySubjectScheduleInline(admin.TabularInline):
    model = LearningDaySubjectSchedule
    exclude = ('creator', 'create_time', 'deleted_at', 'update_time')
    radio_fields = {'day_type': admin.VERTICAL}
    raw_id_fields =('lession_times', )
    autocomplete_lookup_fields = {
        'm2m': ['lession_times'],
    }
    extra = 6
@admin.register(SubjectStudentSchedule)
class SubjectStudentScheduleAdmin(BaseAdmin):
    inlines = [LearningDaySubjectScheduleInline]
    list_display = ('study_session', 'student_schedule', 'subject')
    fieldsets = (
        (None, {'fields': ('study_session', 'student_schedule', 'subject')}),
    )
    # def save_model(self, request, obj, form, change):
    #     super(SubjectStudentScheduleAdmin, self).save_model(request, obj, form, change)    
    #     obj.save()