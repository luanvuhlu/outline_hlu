# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from university.models import Subject
# Create your views here.

class SubjectListView(ListView):
	model = Subject
class SubjectDetailView(DetailView):
	model = Subject