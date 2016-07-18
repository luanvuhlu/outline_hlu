from django.contrib import admin
from common.admin import BaseAdmin
from models import Library, LearningResource, LearningResourceType, Publishing
from django.forms.utils import flatatt
# Register your models here.

@admin.register(Library)
class LibraryAdmin(BaseAdmin):
    class Meta:
        model = Library
@admin.register(Publishing)
class PublishingAdmin(BaseAdmin):
    class Meta:
        model = Publishing
@admin.register(LearningResource)
class LearningResourceAdmin(BaseAdmin):
    class Meta:
        model = LearningResource
@admin.register(LearningResourceType)
class LearningResourceTypeAdmin(BaseAdmin):
    class Meta:
        model = LearningResourceType