# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from datetime import datetime
from models import Outline, Problem, ProblemDetail
from schedule.models import CurrentWeek

# Create your views here.
@login_required(login_url="login/")
def home(request):
	return render(request, 'home.html')
class OutlineListView(ListView):
	model = Outline
class OutlineDetailView(DetailView):
	model = Outline
	def get_context_data(self, **kwargs):
		context = super(OutlineDetailView, self).get_context_data(**kwargs)
		problems = {}
		problem_details = ProblemDetail.objects.filter(problem__outline__id=context['object'].id).select_related('problem')
		for detail in problem_details:
			if detail.problem not in problems:
				problems[detail.problem]=[]
			problems[detail.problem].append(detail)
		context['problems'] = problems
		try:
			current_week = CurrentWeek.objects.get(semester__start_date__lte=datetime.now(), deleted_at__isnull=True)
		except CurrentWeek.DoesNotExist:
			current_week = None
		context['current_week'] = u'Chưa bắt đầu' if not current_week else current_week.current_week_15 if context['object'].study_time_type==0 else current_week.current_week_5
		return context