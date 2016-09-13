# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from models import Outline

# Create your views here.
class OutlineListView(ListView):
	model = Outline