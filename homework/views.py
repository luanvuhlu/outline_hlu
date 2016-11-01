# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from models import HomeWork
# Create your views here.

class HomeWorkDetailView(DetailView):
	model = HomeWork
class HomeWorkListView(ListView):
	model = HomeWork