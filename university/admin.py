# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
# from datetimewidget.widgets import TimeWidget
from models import University, SpecializedStudy, Course, UClass, Subject, Lecturer, Student, Faculty, LessionTime
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
@admin.register(Faculty)
class Faculty(BaseAdmin):
    list_display = ('name', 'university', 'create_time')
    fieldsets = (
        (None, {'fields': ('university', 'name', 'name_abbr', 'address')}),
    )
    class Meta:
        model = Faculty
@admin.register(SpecializedStudy)
class SpecializedStudyAdmin(BaseAdmin):
    list_display = ('name', 'university', 'faculty', 'create_time')
    fieldsets = (
        (None, {'fields': ('university', 'faculty', 'name', 'name_abbr', 'address')}),
    )
    class Meta:
        model = SpecializedStudy
@admin.register(UClass)
class UClassAdmin(BaseAdmin):
    list_display = ('full_name', 'course', 'get_university', 'create_time')
    radio_fields = {'course': admin.VERTICAL}
    fieldsets = (
        (None, {'fields': ('course', 'name', 'name_abbr')}),
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
        (None, {'fields': ('account', 'nick_name')}),
    )
    list_display = ('get_family_name', 'get_name', 'get_email', 'create_time')
    list_display_links = ('get_family_name', 'get_name', 'get_email', )
    raw_id_fields = ('account', )
    autocomplete_lookup_fields = {
        'fk' : ['account', ],
    }
    class Meta:
        model = Lecturer
# class LesstionTimeForm(forms.ModelForm):
#     class Meta:
#         model = LessionTime
#         fields = ('university', 'name', 'order', 'start', 'end')
#         widgets = {
#             'start': TimeWidget(usel10n=True, bootstrap_version=3),
#         }
@admin.register(LessionTime)
class LessionTimeAdmin(BaseAdmin):
    # form = LesstionTimeForm
    fieldsets = (
        (None, {'fields': ('university', 'name', 'order', 'start', 'end')}),
    )
    list_display = ('university', 'name', 'order', 'start', 'end')
    class Meta:
        model = LessionTime
    def save_model(self, request, obj, form, change):
        super(LessionTimeAdmin, self).save_model(request, obj, form, change)        
        if not obj.name:
            obj.name = str(obj.order)
            obj.save()