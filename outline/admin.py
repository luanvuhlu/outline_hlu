# -*- coding: utf-8 -*-
from django.contrib import admin
from common.admin import BaseAdmin
from homework.admin import HomeWorkInine
from schedule.admin import WeekInline
from models import Outline, OutlineLearningResource, Problem, ProblemDetail, AdvisoryTime
# Register your models here.

class ProblemInline(admin.TabularInline):
    model = Problem
    exclude = ('description', 'creator', 'create_time', 'deleted_at', 'update_time')
    extra = 15
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit = False)
        if not change:
            for instance in instances:
                instance.creator=request.user
                instance.save()
        formset.save_m2m()
class OutlineLearningResourceInline(admin.TabularInline):
    model = OutlineLearningResource
    exclude = ('description', 'creator', 'create_time', 'deleted_at', 'update_time')
    radio_fields = {'resource_type': admin.VERTICAL}
    raw_id_fields =('outline', 'learning_resource')
    autocomplete_lookup_fields = {
        'fk': ['learning_resource'],
    }
    extra = 20
class AdvisoryTimeInline(admin.TabularInline):
    model = AdvisoryTime
    exclude = ('description', 'creator', 'create_time', 'deleted_at', 'update_time')
    extra = 3
@admin.register(Outline)
class OutLineAdmin(BaseAdmin):
    inlines = [ProblemInline, OutlineLearningResourceInline, WeekInline,AdvisoryTimeInline, HomeWorkInine]
    radio_fields = {'course': admin.VERTICAL, 'scholastic': admin.VERTICAL}
    list_display = ('subject', 'course_verbose', 'scholastic', 'university_verbose', 'create_time')
    fieldsets = (
        (None, {'fields': ('scholastic', 'subject', 'course')}),
    )
    raw_id_fields =('subject', )
    autocomplete_lookup_fields = {
        'fk': ['subject'],
    }
@admin.register(OutlineLearningResource)
class OutlineLearningResourceAdmin(BaseAdmin):
    list_display = ('learning_resource', 'get_resource_type_display', 'outline', 'create_time')
    radio_fields = {'resource_type': admin.VERTICAL}
    fieldsets = (
        (None, {'fields': ('outline', 'learning_resource', 'resource_type')}),
    )
    raw_id_fields =('outline', 'learning_resource')
    autocomplete_lookup_fields = {
        'fk': ['outline', 'learning_resource'],
    }
    pass
class ProblemDetailInline(admin.TabularInline):
    model = ProblemDetail
    exclude = ('description', 'creator', 'create_time', 'deleted_at', 'update_time')
    extra = 10
@admin.register(Problem)
class ProblemAdmin(BaseAdmin):
    inlines = [ProblemDetailInline, ]
    list_display = ('outline', 'order', 'name', 'university_name', 'create_time')
    fieldsets =(
        (None, {'fields': ('outline', 'order', 'name')}),
    )
    raw_id_fields =('outline', )
    autocomplete_lookup_fields = {
        'fk': ['outline'],
    }
@admin.register(ProblemDetail)
class ProblemDetailAdmin(BaseAdmin):
    list_display = ('content', 'problem', 'order', 'outline_name', 'university_name', 'create_time')
    fieldsets =(
        (None, {'fields': ('problem', 'content', 'order')}),
    )
    raw_id_fields =('problem', )
    autocomplete_lookup_fields = {
        'fk': ['problem'],
    }