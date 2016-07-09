from __future__ import unicode_literals

from django.db import models
from account.models import Account
from common.models import HistoryModel

# Create your models here.
class University(HistoryModel):
    founding=models.DateTimeField(blank=False)
    address_1 = models.CharField(blank=False)
    address_2 = models.CharField(blank=False)
    address_3 = models.CharField(blank=False)
    city = models.CharField(blank=True)
    name = models.CharField(blank=True)
    name_abbr=models.CharField(blank=False)
    user = models.ForeignKey(Account, blank=False)

class SpecializedStudy(HistoryModel):
    address=models.CharField(blank=False)
    university=models.ForeignKey(University, blank=True)
    name = models.CharField(blank=True)
    name_abbr = models.CharField(blank=False)
    user = models.ForeignKey(Account, blank=False)

class Course(HistoryModel):
    university=models.ForeignKey(University, blank=True)
    current_yn=models.BooleanField(blank=True, default=True)
    name = models.CharField(blank=True)
    name_abbr = models.CharField(blank=False)
    user = models.ForeignKey(Account, blank=False)

class UClass(HistoryModel):
    course=models.ForeignKey(Course, blank=True)
    specialized_study=models.ForeignKey(SpecializedStudy, blank=False)
    description=models.CharField(blank=False)
    name = models.CharField(blank=True)
    name_abbr = models.CharField(blank=False)
    user = models.ForeignKey(Account, blank=False)

class Subject(HistoryModel):
    specialized_study=models.ForeignKey(SpecializedStudy, blank=True)
    credit=models.IntegerField(blank=True, default=2)
    description=models.CharField(blank=False)
    name = models.CharField(blank=True)
    name_abbr = models.CharField(blank=False)
    user = models.ForeignKey(Account, blank=False)

class Scholastic(HistoryModel):
    name=models.CharField(blank=True)
    user = models.ForeignKey(Account, blank=False)
class Student(Account):
    nick_name=models.CharField(blank=False)
    u_class=models.ForeignKey(UClass, blank=False)
class Lecturer(Account):
    nick_name=models.CharField(blank=False)
    specialized_study=models.ForeignKey(SpecializedStudy, blank=False)