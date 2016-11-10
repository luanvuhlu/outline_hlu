# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView
from models import HomeWork, HomeWorkQuestion, HomeWorkQuestionAttachment
from forms import HomeWorkQuestionForm
# Create your views here.

class HomeWorkDetailView(DetailView):
	model = HomeWork
class HomeWorkListView(ListView):
	model = HomeWork
class HomeWorkQuestionView(CreateView):
	template_name = "homework/homework_question.html"
	form_class = HomeWorkQuestionForm
	def get_form_kwargs(self):
		kwargs = super(HomeWorkQuestionView, self ).get_form_kwargs()
		kwargs['user'] = self.request.user
		kwargs['home_work_id'] = self.kwargs.get('pk', None)
		return kwargs
	def get_success_url(self):
    		return reverse('homework_question',args=(self.kwargs.get('pk', None)))
	def get_context_data(self, **kwargs):
		context = super(HomeWorkQuestionView, self).get_context_data(**kwargs)
		homework = self.get_homework()
		questions = self.get_questions(homework.id)
		context['homework'] = homework
		context['questions'] = questions
		return context
	def get_questions(self, homework_id):
    		questions = HomeWorkQuestion.objects.filter(home_work__id=homework_id)
		question_attachments = HomeWorkQuestionAttachment.objects.filter(question__home_work__id=homework_id).select_related('question')
		questions_dict={question: [] for question in questions}
		for question_attachment in question_attachments:
			question = question_attachment.question
			questions_dict[question].append(question_attachment)
		return questions_dict
	def get_homework_id(self):
		homework_id = self.kwargs.get('pk', None)
		if not homework_id:
			raise Http404
		return homework_id
	def get_homework(self):
    		homework_id = self.get_homework_id()
		try:
			homework = HomeWork.objects.get(pk=homework_id)
		except HomeWork.DoesNotExist:
			raise Http404
		return homework
	
	