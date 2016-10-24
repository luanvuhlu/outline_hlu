# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
	username = forms.CharField(label=u'Tên đăng nhập', max_length=50,
		widget=forms.TextInput(attrs={'class': 'form-control', name='user-name'}))
	password = forms.CharField(label=u'Mật khẩu', max_length=50,
		widget=forms.TextInput(attrs={'class': 'form-control', name='password'}))

