# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from models import Outline, Problem, ProblemDetail
from schedule.models import CurrentWeek, LearningDayContent, LearningDayRequirement, HomeWorkAction, Week

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
		problems_db = Problem.objects.filter(outline__id=outline_id)
		problems = {problem: [] for problem in problems_db}
		problem_details = ProblemDetail.objects.filter(problem__outline__id=outline_id).select_related('problem')
		for detail in problem_details:
			if detail.problem not in problems:
				problems[detail.problem]=[]
			problems[detail.problem].append(detail)
		return problems
	def get_weeks(self, outline_id):
		weeks_db = Week.objects.filter(outline__id=outline_id)
		weeks = {week: [] for week in weeks_db}
		days = {}
		home_work_actions = HomeWorkAction.objects.filter(week__outline__id=outline_id).select_related('week').select_related('homework')
		learning_day_contents = LearningDayContent.objects.filter(day__week__outline__id=outline_id).select_related('day').select_related('day__week')
		learning_day_requirements = LearningDayRequirement.objects.filter(day__week__outline__id=outline_id).select_related('day').select_related('day__week')
		for learning_day_content in learning_day_contents:
			day = learning_day_content.day
			if day not in days:
				days[day]={}
				days[day]['contents']=[]
				days[day]['requirements']=[]
			days[day]['contents'].append(learning_day_content)
		for learning_day_requirement in learning_day_requirements:
			day = learning_day_requirement.day
			if day not in days:
				days[day]={}
				days[day]['contents']=[]
				days[day]['requirements']=[]
			days[day]['requirements'].append(learning_day_requirement)
		for day, day_content in days.iteritems():
			week = day.week
			if week not in weeks:
				weeks[week]={}
				weeks[week]['days']=[]
				weeks[week]['home_work_actions']=[]
			weeks[week]['days'].append({day: day_content})
		for home_work_action in home_work_actions:
			week = home_work_action.week
			if week not in weeks:
				weeks[week]={}
				weeks[week]['days']=[]
				weeks[week]['home_work_actions']=[]
			weeks[week]['home_work_actions'].append(home_work_action)
		return weeks
	def get_context_data(self, **kwargs):
		context = super(OutlineDetailView, self).get_context_data(**kwargs)
		context['problems'] = self.get_problems(context['object'].id)
		context['current_week'] = self.get_current_week(context['object'].study_time_type)
		context['weeks'] = self.get_weeks(context['object'].id)
		return context