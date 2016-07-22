# -*- coding: utf-8 -*-
from django.contrib import admin
from common.admin import BaseAdmin
from models import Outline, OutlineLearningResource, Problem, ProblemDetail
# Register your models here.

class ProblemInline(admin.StackedInline):
    model = Problem
    exclude = ('creator', 'create_time', 'deleted_at', 'update_time')
    extra = 15
@admin.register(Outline)
class OutLineAdmin(BaseAdmin):
    inlines = [ProblemInline, ]
    pass
@admin.register(OutlineLearningResource)
class OutlineLearningResourceAdmin(BaseAdmin):
    pass
class ProblemDetailInline(admin.StackedInline):
    model = ProblemDetail
    exclude = ('creator', 'create_time', 'deleted_at', 'update_time')
    extra = 5
@admin.register(Problem)
class ProblemAdmin(BaseAdmin):
    inlines = [ProblemDetailInline, ]
@admin.register(ProblemDetail)
class ProblemDetailAdmin(BaseAdmin):
    pass