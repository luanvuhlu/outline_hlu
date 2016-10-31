# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from models import Outline, Problem, ProblemDetail
from schedule.models import CurrentWeek, LearningDayContent, LearningDayRequirement

# Create your views here.
@login_required
def home(request):
	return render(request, 'home.html')
class OutlineListView(ListView):
	model = Outline
class OutlineDetailView(DetailView):
	model = Outline
	def get_current_week(self, study_time_type):
		try:
			current_week = CurrentWeek.objects.get(semester__start_date__lte=datetime.now(), deleted_at__isnull=True)
		except CurrentWeek.DoesNotExist:
			current_week = None
		return u'Chưa bắt đầu' if not current_week else current_week.current_week_15 if study_time_type==0 else current_week.current_week_5
	def get_problems(self, outline_id):
		problems = {}
		problem_details = ProblemDetail.objects.filter(problem__outline__id=outline_id).select_related('problem')
		for detail in problem_details:
			if detail.problem not in problems:
				problems[detail.problem]=[]
			problems[detail.problem].append(detail)
	def get_weeks(self, outline_id):
		weeks = {}
		days = {}
		learning_day_contents = LearningDayContent.objects.filter(day__week__outline__id=outline_id).select_related('day').select_related('day__week')
		learning_day_requirements = LearningDayRequirement.objects.filter(day__week__outline__id=outline_id).select_related('day').select_related('day__week')
		for learning_day_content in learning_day_contents:
			if learning_day_content.day not in days:
				days[learning_day_content.day]={}
				days[learning_day_content.day]['contents']=[]
				days[learning_day_content.day]['requirements']=[]
			days[learning_day_content.day]['contents'].append(learning_day_content)
		for learning_day_requirement in learning_day_requirement:
			if learning_day_requirement.day not in days:
				days[learning_day_requirement.day]={}
				days[learning_day_requirement.day]['contents']=[]
				days[learning_day_requirement.day]['requirements']=[]
			days[learning_day_requirement.day]['requirements'].append(learning_day_requirement)
		for day in days:
			if day.week not in weeks:
				weeks[day.week]=[]
			weeks[day.week].append(day)
		return weeks
	def get_context_data(self, **kwargs):
		context = super(OutlineDetailView, self).get_context_data(**kwargs)
		context['problems'] = self.get_problems(context['object'].id)
		context['current_week'] = self.get_current_week(context['object'].study_time_type)
		context['weeks'] = self.get_weeks(context['object'].id)
		return context