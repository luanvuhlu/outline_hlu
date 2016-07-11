from django.contrib import admin
from common.admin import BaseAdmin
from models import Outline, OutlineLearningResource, SubjectSchedule, Problem, ProblemDetail, Week
# Register your models here.

@admin.register(Outline)
class OutLineAdmin(BaseAdmin):
    pass
@admin.register(OutlineLearningResource)
class OutlineLearningResourceAdmin(BaseAdmin):
    pass
@admin.register(SubjectSchedule)
class SubjectScheduleAdmin(BaseAdmin):
    pass
@admin.register(Problem)
class ProblemAdmin(BaseAdmin):
    pass
@admin.register(ProblemDetail)
class ProblemDetailAdmin(BaseAdmin):
    pass
@admin.register(Week)
class WeekAdmin(BaseAdmin):
    pass