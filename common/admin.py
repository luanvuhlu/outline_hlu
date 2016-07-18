# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

class BaseAdmin(admin.ModelAdmin):
    exclude = ('creator', 'create_time', 'update_time', 'deleted_at')
    readonly_fields = ('creator', 'create_time', 'update_time')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()

    def get_readonly_fields(self, request, obj=None):
        if not obj:  # Add Mode
            exclude_fields=('creator', 'create_time', 'update_time')
            return tuple(field for field in self.readonly_fields if field not in exclude_fields)
        return self.readonly_fields