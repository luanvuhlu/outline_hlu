from django.shortcuts import render
from django.contrib import auth                 
from django.core.context_processors import csrf 
from django.http import HttpResponseRedirect
from forms import SignUpForm
# Create your views here.
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	context = {}
	context.update(csrf(request))
	context['form'] = SignUpForm()
	reteurn render(request, 'register.html', context)