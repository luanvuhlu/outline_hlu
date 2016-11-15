# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django.contrib import admin
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.http.response import HttpResponseRedirect, Http404
from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView
from django.utils.decorators import method_decorator
from django.db import transaction, IntegrityError
from common.admin import BaseAdmin
from common.models import BaseModel
from account.models import CreatorModel
from models import Scholastic, SubjectSchedule, LearningDay, LearningDayContent, LearningDayRequirement, HomeWorkAction, StudySession, Semester, Week
from forms import WeekGenerateForm
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)
# Register your models here.
@method_decorator(staff_member_required, name='dispatch')
class WeekGenerateView(FormView):
    template_name = "admin/schedule/week/generate.html"
    form_class = WeekGenerateForm
    def form_valid(self, form):
        raw_semester_id = form.cleaned_data.get('semester', None)
        if not raw_semester_id:
            logger.error(u'Không tìm thấy thông tin học kỳ')
            raise Http404
        semester_id = int(raw_semester_id)
        try:
            with transaction.atomic():
                Week.objects.filter(semester__id=semester_id).delete()
                weeks = []
                if not weeks:
                    logger.error(u'Không có tuần nào được tạo')
                    raise Http404
                semester = get_object_or_404(Semester, semester__id=semester_id)
                Week.objects.bulk_create(weeks)
        except IntegrityError as e:
            logger.error(u'Đã có lỗi xảy ra, vui lòng thử lại: %s' % e.message)
            raise e        
        # Xóa những tuần cũ
        
        # Tạo những tuần mới
        
        
        return super(WeekGenerateView, self).form_valid(form)
    def get_context_data(self, *args, **kwargs):
        context = super(WeekGenerateView, self).get_context_data(*args, **kwargs)
        return context
    def get_success_url(self):
        return reverse("admin:schedule_week_changelist")
@admin.register(Week)
class WeekAdmin(BaseAdmin):
    change_list_template = "admin/schedule/week/change_list.html"
    models = Week
    actions = ['delete_selected']
    list_display = ('semester', 'order', 'other_order', 'start_date', 'end_date', 'holiday')
    fieldsets = (
        (None, {'fields': ('semester', 'order', 'other_order', 'start_date', 'end_date', 'holiday')}),
    )
    readonly_fields = ('semester', 'order', 'other_order', 'start_date', 'end_date',)
    def get_urls(self):
        urls = super(WeekAdmin, self).get_urls()
        my_urls = patterns("",
            url(r"^generate/$", WeekGenerateView.as_view())
        )
        return my_urls + urls
class HomeWorkActionInline(admin.TabularInline):
    model = HomeWorkAction
    exclude = ('creator', 'create_time', 'deleted_at', 'update_time')
    extra = 5
class LearningDayInline(admin.TabularInline):
    model = LearningDay
    radio_fields = {'day_type': admin.VERTICAL, 'order': admin.VERTICAL}
    exclude = ('creator', 'create_time', 'deleted_at', 'update_time')
    extra = 3
# class WeekInline(admin.TabularInline):
#     model = Week
#     exclude = ('creator', 'create_time', 'deleted_at', 'update_time')
#     extra = 16
# @admin.register(Week)
# class WeekAdmin(BaseAdmin):
#     inlines = [HomeWorkActionInline]
#     list_display = ('outline', 'order', 'university_name', 'create_time')
#     fieldsets = (
#         (None, {'fields': ('outline', 'order')}),
#     )
#     raw_id_fields =('outline', )
#     autocomplete_lookup_fields = {
#         'fk': ['outline'],
#     }
#     ordering = ('outline', 'order')
#     search_fields = ['outline__subject__name', '=order', '^outline__scholastic__name', 'outline__course__university__name']
#     list_filter = (
#         ('order'),
#     )
@admin.register(SubjectSchedule)
class SubjectScheduleAdmin(BaseAdmin):
    model = SubjectSchedule
    list_display = ('outline', 'week')
    fieldsets = (
        (None, {'fields': ('outline', 'week')}),
    )
class LearningDayContentInline(admin.TabularInline):
    model = LearningDayContent
    exclude = ('creator', 'create_time', 'deleted_at', 'update_time')
    extra = 5
class LearningDayRequirementInline(admin.TabularInline):
    model = LearningDayRequirement
    exclude = ('creator', 'create_time', 'deleted_at', 'update_time')
    extra = 5
@admin.register(LearningDay)
class LearningDayAdmin(BaseAdmin):
    inlines = [LearningDayContentInline, LearningDayRequirementInline]
    list_display = ('outline_name', 'week', 'day_type', 'order', 'university_name', 'create_time')
    fieldsets = (
        (None, {'fields': ('week', 'day_type', 'order')}),
    )
    radio_fields = {'order' : admin.VERTICAL}
    # readonly_fields = ('outline_name', 'university_name', )
class StudySessionInline(admin.TabularInline):
    model = StudySession
    exclude = ('creator', 'create_time', 'deleted_at', 'update_time')
    extra = 4
    #TODO add start_date and end_date
@admin.register(Scholastic)
class ScholasticAdmin(BaseAdmin):
    list_display = ('name', 'start_date', 'end_date', 'create_time')
    readonly_fields = ('name', )
    fieldsets = (
        (None, {'fields': ('name', 'start_date', 'end_date')}),
    )
    def save_model(self, request, obj, form, change):
        obj.name = '%s-%s' % (obj.start_date.year, obj.end_date.year)
        BaseAdmin.save_model(self, request, obj, form, change)
    class Meta:
        model = Scholastic
@admin.register(Semester)
class SemesterAdmin(BaseAdmin):
    inlines = [StudySessionInline]
    list_display = ('order', 'scholastic', 'start_date', 'end_date', 'university', 'create_time')
    fieldsets = (
        (None, {'fields': ('university', 'scholastic', 'order', ('start_date', 'end_date'))}),
    )
    radio_fields = {'order': admin.HORIZONTAL}
    class Meta:
        model = Semester
    def save_model(self, request, obj, form, change):
        if not obj.start_date:
            obj.start_date = obj.scholastic.start_date
        if not obj.end_date:
            obj.end_date = obj.scholastic.end_date
        BaseAdmin.save_model(self, request, obj, form, change)
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if not instance.start_date:
                instance.start_date = instance.semester.start_date
            if not instance.end_date:
                instance.end_date = instance.semester.end_date
            if isinstance(instance, BaseModel):
                instance.update_time = timezone.now()
            if isinstance(instance, CreatorModel) and not instance.creator_id:
                instance.creator = request.user
            instance.save()
@admin.register(StudySession)
class StudySessionAdmin(BaseAdmin):
    list_display = ('semester', 'order', 'start_date', 'end_date', 'create_time')
    fieldsets = (
        (None, {'fields': ('semester', 'order', ('start_date', 'end_date'))}),
    )
    radio_fields = {'order': admin.HORIZONTAL}
    def save_model(self, request, obj, form, change):
        if not obj.start_date:
            obj.start_date = obj.semester.start_date
        if not obj.end_date:
            obj.end_date = obj.semester.end_date
        BaseAdmin.save_model(self, request, obj, form, change)
    class Meta:
        model = StudySession
# @admin.register(CurrentWeek)
# class CurrentWeekAdmin(BaseAdmin):
#     list_display = ('semester', 'university_name', 'current_week_15', 'current_week_5', 'start_date', 'end_date', 'create_time')
#     fieldsets = (
#         (None, {'fields': ('semester', ('start_date', 'end_date'), 'current_week_15', 'current_week_5')}),
#     )

    # readonly_fields = ('start_date', 'end_date')
# @admin.register(LearningDayContent)
# class LearningDayContentAdmin(BaseAdmin):
#     pass
# @admin.register(LearningDayRequirement)
# class LearningDayRequirementAdmin(BaseAdmin):
#     pass
# @admin.register(HomeWorkAction)
# class HomeWorkActionAdmin(BaseAdmin):
#     pass
