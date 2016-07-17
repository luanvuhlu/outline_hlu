# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

class BaseAdmin(admin.ModelAdmin):
    exclude = ('creator', 'create_time','deleted_at', 'update_time')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()