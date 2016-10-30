# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
# from django.contrib.auth.mixins import LoginRequiredMixin
from university.models import Subject, SpecializedStudy
from outline.models import Outline
# Create your views here.

class SubjectListView(ListView):
	model = Subject
class SubjectDetailView(DetailView):
	model = Subject
	def get_context_data(self, **kwargs):
		context = super(SubjectDetailView, self).get_context_data(**kwargs)
		context['outlines'] = Outline.objects.filter(subject__id=context['object'].id)
		return context
class SpecializedStudyListView(ListView):
	model = SpecializedStudy
class SpecializedStudyDetailView(DetailView):
	model = SpecializedStudy
	def get_context_data(self, **kwargs):
		context = super(SpecializedStudyDetailView, self).get_context_data(**kwargs)
		context['subjects'] = Subject.objects.filter(specialized_study__id=context['object'].id)
		return context