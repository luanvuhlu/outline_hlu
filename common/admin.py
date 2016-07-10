from django.contrib import admin

# Register your models here.

class BaseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()