# -*- coding: utf-8 -*-
from django.contrib import admin
from models import University, SpecializedStudy, Scholastic, Course, UClass, Subject, Student, Lecturer
from common.admin import BaseAdmin
# Register your models here.

@admin.register(University)
class UniversityAdmin(BaseAdmin):
    readonly_fields = ('creator', )
    exclude = ('deleted_at',)
    class Meta:
        model = University

@admin.register(Course)
class CourseAdmin(BaseAdmin):
    readonly_fields = ('creator', )
    exclude = ('deleted_at',)
    class Meta:
        model = Course
