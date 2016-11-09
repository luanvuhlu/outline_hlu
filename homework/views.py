# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView
from models import HomeWork, HomeWorkQuestion, HomeWorkQuestionAttachment
# Create your views here.

class HomeWorkDetailView(DetailView):
	model = HomeWork
class HomeWorkListView(ListView):
	model = HomeWork
class HomeWorkQuestionCreate(TemplateView):
	template_name = "homework/homework_question_create.html"
	def get_context_data(self, **kwargs):
		context = super(HomeWorkQuestionCreate, self).get_context_data(**kwargs)
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
	def get(self, request, *args, **kwargs):
    		self.kwargs.get('pk', None)
		return super(HomeWorkQuestionCreate, self).get(request, *args, **kwargs)
	def post(self, request, *args, **kwargs):
		return super(HomeWorkQuestionCreate, self).get(request, *args, **kwargs)
	
	