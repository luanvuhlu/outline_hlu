# -*- coding: utf-8 -*-
from django.contrib import admin
from common.admin import BaseAdmin
from university.models import Scholastic
from models import Outline, OutlineLearningResource, Problem, ProblemDetail
# Register your models here.

class ProblemInline(admin.TabularInline):
    model = Problem
    exclude = ('creator', 'create_time', 'deleted_at', 'update_time')
    extra = 15
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit = False)
        if not change:
            for instance in instances:
                instance.creator=request.user
                instance.save()
        formset.save_m2m()
@admin.register(Outline)
class OutLineAdmin(BaseAdmin):
    inlines = [ProblemInline, ]
    list_display = ('subject', 'course_verbose', 'scholastic', 'create_time')
    fieldsets = (
        (None, {'fields': ('scholastic', 'subject', 'course')}),
    )
    
@admin.register(OutlineLearningResource)
class OutlineLearningResourceAdmin(BaseAdmin):
    
    pass
class ProblemDetailInline(admin.TabularInline):
    model = ProblemDetail
    exclude = ('creator', 'create_time', 'deleted_at', 'update_time')
    extra = 5
@admin.register(Problem)
class ProblemAdmin(BaseAdmin):
    inlines = [ProblemDetailInline, ]
    list_display = ('outline', 'order', 'name', 'create_time')
    fieldsets =(
        (None, {'fields': ('outline', 'order', 'name')}),
    )
@admin.register(ProblemDetail)
class ProblemDetailAdmin(BaseAdmin):
    pass