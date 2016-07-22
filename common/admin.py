# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils import timezone
from models import BaseModel
from account.models import CreatorModel
# Register your models here.

class BaseAdmin(admin.ModelAdmin):
    exclude = ('creator', 'create_time', 'update_time', 'deleted_at')
    readonly_fields = ('creator', 'create_time', 'update_time')
    fieldsets = (
        (u'Lịch sử', {'fields': ('creator', 'create_time', 'update_time',)}),
    )
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        else:
            obj.update_time = timezone.now()
        obj.save()
    def get_fieldsets(self, request, obj=None):
        # Nếu là form sửa, thêm thông tin lịch sử
        if obj and self.fieldsets != BaseAdmin.fieldsets:
            return self.fieldsets + BaseAdmin.fieldsets
        return self.fieldsets
    def get_readonly_fields(self, request, obj=None):
        if not obj:  # Add Mode
            exclude_fields=('creator', 'create_time', 'update_time')
            return tuple(field for field in self.readonly_fields if field not in exclude_fields)
        return self.readonly_fields
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, BaseModel):
                instance.update_time = timezone.now()
            if isinstance(instance, CreatorModel) and not instance.creator_id:
                instance.creator = request.user
            instance.save()