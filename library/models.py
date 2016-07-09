from __future__ import unicode_literals

from django.db import models
from account.models import Account
from common.models import HistoryModel
from university.models import UClass, SpecializedStudy, Scholastic, Subject, Course, University

# Create your models here.
class Library(HistoryModel):
    university=models.ForeignKey(University, blank=False)
    user = models.ForeignKey(Account, blank=False)
    name=models.CharField(blank=True)
    name_abbr=models.CharField(blank=False)
    address_1 = models.CharField(blank=False)
    address_2=models.CharField(blank=False)
    address_3=models.CharField(blank=False)
    city=models.CharField(blank=True)

class LearningResourceType(HistoryModel):
    name=models.CharField(blank=True)
    user = models.ForeignKey(Account, blank=False)
class LearningResource(HistoryModel):
    name=models.CharField(blank=True)
    library=models.ForeignKey(Library, blank=True)
    resource_type=models.ForeignKey(LearningResourceType, blank=True)
    avaiable_yn=models.BooleanField(blank=True, default=True)
    buy_yn=models.BooleanField(blank=True, default=False)
    buy_place=models.CharField(blank=False)
    borrow_yn=models.BooleanField(blank=True, default=True)
    borrow_place=models.CharField(blank=False)
    user = models.ForeignKey(Account, blank=False)