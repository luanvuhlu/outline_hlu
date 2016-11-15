# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.contrib.admin import SimpleListFilter, RelatedFieldListFilter
from django.contrib import admin
from models import University
class BaseUniversityListFilter(admin.SimpleListFilter):
    title = _(u'Đại học')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'university'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return University.objects.values_list('id', 'name')