# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('creator', 'create_time',)
    exclude = ('deleted_at', 'update_time')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()