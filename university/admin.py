# -*- coding: utf-8 -*-
from django.contrib import admin
from models import University, SpecializedStudy, Scholastic, Course, UClass, Subject, Lecturer, Student
from common.admin import BaseAdmin
# Register your models here.

@admin.register(University)
class UniversityAdmin(BaseAdmin):
    class Meta:
        model = University

@admin.register(Course)
class CourseAdmin(BaseAdmin):
    class Meta:
        model = Course
@admin.register(SpecializedStudy)
class SpecializedStudyAdmin(BaseAdmin):
    class Meta:
        model = SpecializedStudy
@admin.register(Scholastic)
class ScholasticAdmin(BaseAdmin):
    class Meta:
        model = Scholastic
@admin.register(UClass)
class UClassAdmin(BaseAdmin):
    class Meta:
        model = UClass
@admin.register(Subject)
class SubjectAdmin(BaseAdmin):
    class Meta:
        model = Subject
@admin.register(Student)
class StudentAdmin(BaseAdmin):
    class Meta:
        model = Student
@admin.register(Lecturer)
class StudentAdmin(BaseAdmin):
    class Meta:
        model = Lecturer
