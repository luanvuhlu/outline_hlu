from django.contrib import admin
from models import Outline
# Register your models here.

class OutLineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Outline, OutLineAdmin)