# -*- coding: utf-8 -*-
from django.contrib import admin
from models import University, SpecializedStudy, Scholastic, Course, UClass, Subject, Lecturer, Student
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
    fieldsets = (
        (None, {'fields': ('university', 'name', 'name_abbr')}),
    )
    class Meta:
        model = Course
@admin.register(SpecializedStudy)
class SpecializedStudyAdmin(BaseAdmin):
    fieldsets = (
        (None, {'fields': ('university', 'name', 'name_abbr', 'address')}),
    )
    class Meta:
        model = SpecializedStudy
@admin.register(Scholastic)
class ScholasticAdmin(BaseAdmin):
    fieldsets = (
        (None, {'fields': ('name', )}),
    )
    class Meta:
        model = Scholastic
@admin.register(UClass)
class UClassAdmin(BaseAdmin):
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
    class Meta:
        model = Subject
@admin.register(Student)
class StudentAdmin(BaseAdmin):
    fieldsets = (
        (None, {'fields': ('account', 'u_class', 'nick_name')}),
    )
    class Meta:
        model = Student
@admin.register(Lecturer)
class LecturerAdmin(BaseAdmin):
    fieldsets = (
        (None, {'fields': ('account', 'nick_name')}),
    )
    class Meta:
        model = Lecturer
