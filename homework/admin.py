# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from common.admin import BaseAdmin
from models import HomeWorkFormat, HomeWork, HomeWorkQuestion, HomeWorkQuestionAttachment, HomeWorkSolution, HomeWorkSolutionAttachment
# Register your models here.
@admin.register(HomeWorkFormat)
class HomeWorkFormatAdmin(BaseAdmin):
    list_display = ('name', 'create_time')
    list_display_links = ('name', )
    fieldsets =(
        (None, {'fields': ('name', ('font', 'page_size'), 'size_unit', ('top_margin', 'bottom_margin', 'left_margin', 'right_margin'), 'break_lines')}),
        (u'Yêu cầu khác', {'fields': ('other', )})
    )
@admin.register(HomeWork)
class HomeWorkAdmin(BaseAdmin):
    list_display = ('type_order_name', 'outline', 'university_name', 'create_time')
    list_display_links = ('type_order_name', )
    fieldsets =(
        (None, {'fields': ('outline', ('hw_type', 'order'), ('page_limit_start', 'page_limit_end'), 'hw_format')}),
        (u'Yêu cầu khác', {'fields': ('handwritten', 'is_not_presenstation_required', 'presentation', 'other_requirement')})
    )
class HomeWorkInine(admin.TabularInline):
    model = HomeWork
    exclude = ('other_requirement', 'presentation', 'is_not_presenstation_required', 'description', 'creator', 'create_time', 'deleted_at', 'update_time')
    extra = 5
# DEBUG
class HomeWorkQuestionAttachmentInline(admin.TabularInline):
    model = HomeWorkQuestionAttachment
    exclude = ('description', 'creator', 'create_time', 'deleted_at', 'update_time')
    extra = 5
# class HomeWorkQuestionForm(forms.ModelForm):
#     class Meta:
#         model = HomeWorkQuestion
#     def clean(self):
#         data = self.cleaned_data
#         if not data.get('content', None):
#             raise forms.ValidationError(u'Bạn phải nhập nội dung hoặc đính kèm file')
@admin.register(HomeWorkQuestion)
class HomeWorkQuestionAdmin(BaseAdmin):
    list_display = ('home_work', 'no', 'content')
    fieldsets = (
        (None, {'fields': ('home_work', 'no', 'content')}),
    )
    inlines = [HomeWorkQuestionAttachmentInline]
    # form = HomeWorkQuestionForm
    def save_model(self, request, obj, form, change):
        super(HomeWorkQuestionAdmin, self).save_model(request, obj, form, change)        
        if not obj.no:
            obj.no = u'Tất cả'
            obj.save()

