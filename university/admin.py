# -*- coding: utf-8 -*-
from django.contrib import admin
from models import University, SpecializedStudy, Scholastic, Course, UClass, Subject, Lecturer, Student
from common.admin import BaseAdmin
# Register your models here.

@admin.register(University)
class UniversityAdmin(BaseAdmin):
    readonly_fields = ('creator', 'create_time', )
    exclude = ('deleted_at', 'update_time')
    class Meta:
        model = University

@admin.register(Course)
class CourseAdmin(BaseAdmin):
    readonly_fields = ('creator', 'create_time')
    exclude = ('deleted_at', 'update_time')
    class Meta:
        model = Course
@admin.register(SpecializedStudy)
class SpecializedStudyAdmin(BaseAdmin):
    readonly_fields = ('creator', 'create_time')
    exclude = ('deleted_at', 'update_time')
    class Meta:
        model = SpecializedStudy
@admin.register(Scholastic)
class ScholasticAdmin(BaseAdmin):
    readonly_fields = ('creator', 'create_time')
    exclude = ('deleted_at', 'update_time')
    class Meta:
        model = Scholastic
@admin.register(UClass)
class UClassAdmin(BaseAdmin):
    readonly_fields = ('creator', 'create_time')
    exclude = ('deleted_at', 'update_time')
    class Meta:
        model = UClass
@admin.register(Subject)
class SubjectAdmin(BaseAdmin):
    readonly_fields = ('creator', 'create_time')
    exclude = ('deleted_at', 'update_time')
    class Meta:
        model = Subject
@admin.register(Student)
class StudentAdmin(BaseAdmin):
    readonly_fields = ('creator', 'create_time')
    exclude = ('deleted_at', 'update_time')
    class Meta:
        model = Student
@admin.register(Lecturer)
class StudentAdmin(BaseAdmin):
    readonly_fields = ('creator', 'create_time')
    exclude = ('deleted_at', 'update_time')
    class Meta:
        model = Lecturer
