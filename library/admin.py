from django.contrib import admin
from common.admin import BaseAdmin
from models import Library, LearningResource, LearningResourceType
from django.forms.utils import flatatt
# Register your models here.

@admin.register(Library)
class LibraryAdmin(BaseAdmin):
    readonly_fields = ('creator', 'create_time', )
    exclude = ('deleted_at', 'update_time')
    class Meta:
        model = Library

@admin.register(LearningResource)
class LearningResourceAdmin(BaseAdmin):
    readonly_fields = ('creator', 'create_time')
    exclude = ('deleted_at', 'update_time')
    class Meta:
        model = LearningResource
@admin.register(LearningResourceType)
class LearningResourceTypeAdmin(BaseAdmin):
    readonly_fields = ('creator', 'create_time')
    exclude = ('deleted_at', 'update_time')
    class Meta:
        model = LearningResourceType