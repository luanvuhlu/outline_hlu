from django.shortcuts import render
from django.contrib import auth                 
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from forms import SignUpForm
# Create your views here.

class RegistrationView(FormView):
	template_name = 'account/register.html'
	form_class = SignUpForm
	success_url = '/'
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return HttpResponseRedirect(self.success_url)
		return super(RegistrationView, self).get(request, *args, **kwargs)
	