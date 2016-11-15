# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from models import Semester
class WeekGenerateForm(forms.Form):
    semester = forms.ModelChoiceField(queryset=Semester.objects.all(), label=u'Học kỳ')