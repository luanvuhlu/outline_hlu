# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from models import Account

class LoginForm(AuthenticationForm):
	username = forms.CharField(label=u'Tên đăng nhập', max_length=50,
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'user-name'}))
	password = forms.CharField(label=u'Mật khẩu', max_length=50,
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class SignUpForm(UserCreationForm):
	class Meta:
		model = Account
		fields = ('family_name', 'name', 'email', 'password1', 'password2', 'date_of_birth', 'address_1', 'address_2', 'address_3', 'city')
	def save(self, commit = True):
		user = super(SignUpForm, self).save(commit = False)
		if commit:
			user.save()
		return user