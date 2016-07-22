# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from common.admin import BaseAdmin
from models import Week, SubjectSchedule, LearningDay, LearningDayContent, LearningDayRequirement, HomeWorkAction
# Register your models here.
@admin.register(Week)
class WeekAdmin(BaseAdmin):
    pass
@admin.register(SubjectSchedule)
class SubjectScheduleAdmin(BaseAdmin):
    pass
@admin.register(LearningDay)
class LearningDayAdmin(BaseAdmin):
    pass
@admin.register(LearningDayContent)
class LearningDayContentAdmin(BaseAdmin):
    pass
@admin.register(LearningDayRequirement)
class LearningDayRequirementAdmin(BaseAdmin):
    pass
@admin.register(HomeWorkAction)
class HomeWorkActionAdmin(BaseAdmin):
    pass