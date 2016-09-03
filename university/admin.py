# -*- coding: utf-8 -*-
from django.contrib import admin
from models import University, SpecializedStudy, Scholastic, Course, UClass, Subject, Lecturer, Student, StudySession, Semester
from common.admin import BaseAdmin
# Register your models here.

@admin.register(University)
class UniversityAdmin(BaseAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'name_abbr', 'founding','address_1', 'address_2','address_3','city',)}),
    )
    class Meta:
        model = University

@admin.register(Course)
class CourseAdmin(BaseAdmin):
    list_display = ('name', 'university', 'create_time')
    fieldsets = (
        (None, {'fields': ('university', 'name', 'name_abbr')}),
    )
    class Meta:
        model = Course
@admin.register(SpecializedStudy)
class SpecializedStudyAdmin(BaseAdmin):
    list_display = ('name', 'university', 'create_time')
    fieldsets = (
        (None, {'fields': ('university', 'name', 'name_abbr', 'address')}),
    )
    class Meta:
        model = SpecializedStudy
class StudySessionInline(admin.TabularInline):
    model = StudySession
    exclude = ('description', 'creator', 'create_time', 'deleted_at', 'update_time')
    extra = 4
@admin.register(Scholastic)
class ScholasticAdmin(BaseAdmin):
    list_display = ('name', 'start_date', 'end_date', 'create_time')
    fieldsets = (
        (None, {'fields': ('name', 'start_date', 'end_date')}),
    )
    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields+('name',)
    def save_model(self, request, obj, form, change):
        obj.name = '%s-%s' % (obj.start_date.year, obj.end_date.year)
        BaseAdmin.save_model(self, request, obj, form, change)
    class Meta:
        model = Scholastic
@admin.register(Semester)
class SemesterAdmin(BaseAdmin):
    inlines = [StudySessionInline]
    list_display = ('scholastic', 'order', 'start_date', 'end_date', 'create_time')
    fieldsets = (
        (None, {'fields': ('scholastic', 'order', ('start_date', 'end_date'))}),
    )
    radio_fields = {'order': admin.HORIZONTAL}
    class Meta:
        model = Semester
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
@admin.register(UClass)
class UClassAdmin(BaseAdmin):
    list_display = ('full_name', 'course', 'specialized_study', 'get_university', 'create_time')
    radio_fields = {'course': admin.VERTICAL, 'specialized_study':  admin.VERTICAL}
    fieldsets = (
        (None, {'fields': ('course', 'specialized_study', 'name', 'name_abbr')}),
    )
    class Meta:
        model = UClass

@admin.register(Subject)
class SubjectAdmin(BaseAdmin):
    fieldsets = (
        (None, {'fields': ('specialized_study', 'name', 'name_abbr', 'credit')}),
    )
    list_display = ('name', 'specialized_study', 'get_university', 'credit', 'create_time')
    radio_fields = {"credit": admin.VERTICAL}
    raw_id_fields = ('specialized_study', )
    autocomplete_lookup_fields = {
        'fk' : ['specialized_study'],
    }
    class Meta:
        model = Subject
@admin.register(Student)
class StudentAdmin(BaseAdmin):
    fieldsets = (
        (None, {'fields': ('account', 'u_class', 'nick_name')}),
    )
    raw_id_fields = ('u_class', 'account', )
    list_display = ('get_family_name', 'get_name', 'get_email', 'create_time', )
    autocomplete_lookup_fields = {
        'fk' : ['u_class', 'account'],
    }
    class Meta:
        model = Student
@admin.register(Lecturer)
class LecturerAdmin(BaseAdmin):
    fieldsets = (
        (None, {'fields': ('account', 'specialized_study', 'nick_name')}),
    )
    list_display = ('get_family_name', 'get_name', 'get_email', 'create_time')
    list_display_links = ('get_family_name', 'get_name', 'get_email', )
    raw_id_fields = ('account', 'specialized_study', )
    autocomplete_lookup_fields = {
        'fk' : ['account', 'specialized_study'],
    }
    class Meta:
        model = Lecturer
