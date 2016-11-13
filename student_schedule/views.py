# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django.db import transaction, IntegrityError
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView
from forms import StudentScheduleChoiceForm, OutlineForSubjectChoiceForm
from models import StudentSchedule, TempStudentScheduleGenerator, TempSubjectStudentScheduleGenerator

logger = logging.getLogger(__name__)
# Create your views here.
# class StudentScheduleCreateView(CreateView):
#     template_name = "student_schedule/student_schedule_generator.html"
#     form_class = StudentScheduleCreateForm
#     def get_success_url(self):
#         return reverse("student_schedule_generator_choice_2")
#     def get_form_kwargs(self):
#         kwargs = super(StudentScheduleCreateView, self ).get_form_kwargs()
#         kwargs['user'] = self.request.user
#         return kwargs

class StudentScheduleGeneratorChoiceView(FormView):
    template_name = "student_schedule/student_schedule_generator.html"
    form_class = StudentScheduleChoiceForm
    def get_success_url(self):
        if self.step == 2:
            return reverse("student_schedule_generator_choice_3")
        return reverse("student_schedule_generator_choice_2")
    # def __init__(self, *args, **kwargs):
    #     super(StudentScheduleGeneratorChoiceView, self).__init__(*args, **kwargs)
    def get_form_kwargs(self):
        kwargs = super(StudentScheduleGeneratorChoiceView, self ).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    # def __init__(self, *args, **kwargs):
    #     super(StudentScheduleGeneratorChoiceView, self).__init__(*args, **kwargs)
    def form_valid(self, form):
        student_schedule_id = form.cleaned_data.get('student_schedule', None)
        if not student_schedule_id:
            raise Http404
        student_schedule = get_object_or_404(StudentSchedule, pk=student_schedule_id)
        # Lấy temp hiện tại hoặc tạo mới
        temp = self.get_or_create_temp(student_schedule, self.request.user)
        # Cập nhật tất cả các temp khác
        TempStudentScheduleGenerator.objects.filter(student=student_schedule.student).exclude(id=temp.id).update(done=True)
        self.step = temp.step
        return super(StudentScheduleGeneratorChoiceView, self).form_valid(form)
    def get_or_create_temp(self, student_schedule, user):
        temp, created = TempStudentScheduleGenerator.objects.get_or_create(student=student_schedule.student,
                                                student_schedule=student_schedule,
                                                done=False, 
                                                defaults = {'creator': user})
        return temp
class AbstractStudentScheduleGenerator(FormView):
    def __init__(self, *args, **kwargs):
        super(AbstractStudentScheduleGenerator, self).__init__(*args, **kwargs)
    def get(self, *args, **kwargs):
        self.check_step_or_redirect(self.request.user)
        return super(AbstractStudentScheduleGenerator, self).get(*args, **kwargs)
    def get_view_step(self):
        pass
    def get_current_temp_step(self, user):
        try:
            step = TempStudentScheduleGenerator.objects.values_list('step', flat=True).get(student_schedule__student__account__id=user.id, done=False)
            return int(step)
        except TempStudentScheduleGenerator.DoesNotExist:
            return 0
    def check_step_or_redirect(self, user):
        current_step = self.get_current_temp_step(user)
        view_step = self.get_view_step()
        if view_step == current_step + 1:
            return
        url = "student_schedule_generator_choice_1"
        if view_step == 1:
            return reverse("student_schedule_generator_choice_2")
        if view_step == 2:
            return reverse("student_schedule_generator_choice_3")
        return reverse(url)
    def get_success_url(self):
        view_step = self.get_view_step()
        url = "student_schedule_generator_choice_3"
        if view_step == 2:
            return reverse("student_schedule_generator_choice_3")
        if view_step == 3:
            return reverse("student_schedule_generator_choice_4")   #DEBUG
        return reverse(url)
class StudentScheduleGeneratorOutlineForSubjectView(AbstractStudentScheduleGenerator):
    template_name = "student_schedule/student_schedule_generator.html"
    form_class = OutlineForSubjectChoiceForm
    def get_form_kwargs(self):
        kwargs = super(StudentScheduleGeneratorOutlineForSubjectView, self ).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['student_schedule_id'] = self.get_student_schedule_id_from_current_temp(self.request.user)
        return kwargs
    def get_view_step(self):
        return 2
    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        # student_schedule_id = self.get_student_schedule_id_from_current_temp(self.request.user)
        outline_ids = []
        for name, id in cleaned_data.iteritems():
            if not name.startswith('outline_'):
                continue
            outline_ids.append(int(id))
        temp = self.get_current_temp(self.request.user)
        temp.step = 2
        try:
            with transaction.atomic():
                temp.save()
                # Create new TempSubjectStudentScheduleGenerator
                for outline_id in outline_ids:
                    TempSubjectStudentScheduleGenerator.objects.create(temp_student_schedule=temp, outline_id=outline_id, creator=self.request.user)
        except IntegrityError as e:
            logger.error(u'Đã có lỗi xảy ra, vui lòng thử lại: %s' % e.message)
            raise e        
        return super(StudentScheduleGeneratorOutlineForSubjectView, self).form_valid(form)
    def get_current_temp(self, user):
        return get_object_or_404(TempStudentScheduleGenerator, student_schedule__student__account__id=user.id, done=False, step=1)
    def get_student_schedule_id_from_current_temp(self, user):
        try:
            return TempStudentScheduleGenerator.objects.values_list('student_schedule__id', flat=True).get(student_schedule__student__account__id=user.id, done=False)
        except TempStudentScheduleGenerator.DoesNotExist:
            return None
    
