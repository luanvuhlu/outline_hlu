# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import Account
from common.models import HistoryModel
from university.models import UClass, SpecializedStudy, Scholastic, Subject, Course
from library.models import LearningResource

# Create your models here.
class Outline(HistoryModel):
    scholastic=models.ForeignKey(Scholastic, blank=True)
    subject=models.ForeignKey(Subject, blank=True)
    course=models.ForeignKey(Course, blank=True)
    description=models.CharField(blank=False)
    user = models.ForeignKey(Account, blank=False)

class OutlineLearningResource(HistoryModel):
    outline=models.ForeignKey(Outline, blank=True)
    learning_resource=models.ForeignKey(LearningResource, blank=False)
    resource_type=models.CharField(blank=True) # Loại tài liệu
    user = models.ForeignKey(Account, blank=False)

class Problem(HistoryModel):
    name=models.CharField(blank=True)
    description=models.CharField(blank=False)
    user = models.ForeignKey(Account, blank=False)

class ProblemDetail(HistoryModel):
    problem=models.ForeignKey(Problem, blank=True)
    content=models.CharField(blank=True)
    description=models.CharField(blank=False)

class Week(HistoryModel):
    outline=models.ForeignKey(Outline, blank=True)
    order=models.IntegerField(blank=True)
    description=models.CharField(blank=False)
    user = models.ForeignKey(Account, blank=False)

class SubjectSchedule(HistoryModel):
    outline=models.ForeignKey(Outline, blank=True)
    week=models.ForeignKey(Week, blank=True)
    user = models.ForeignKey(Account, blank=False)
