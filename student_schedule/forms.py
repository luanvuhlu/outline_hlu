# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django import forms
from django.db import transaction, IntegrityError
from account.models import Account
from outline.models import Outline
from university.models import Student
from models import StudentSchedule, SubjectStudentSchedule, TempStudentScheduleGenerator

logger = logging.getLogger(__name__)

class AbstractStudentScheduleGeneratorForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AbstractStudentScheduleGeneratorForm, self).__init__(*args, **kwargs)
    
    def create_new_temp_student_schedule(self, user):
        student_id = Student.objects.values_list('id', flat=True).get(account__id=user.id)
        student = Student(id=student_id)
        TempStudentScheduleGenerator.objects.create(student=student, creator=user)
class StudentScheduleChoiceForm(AbstractStudentScheduleGeneratorForm):
    student_schedule = forms.ChoiceField(label=u'Lịch học',
                                        required=True)
    def __init__(self, *args, **kwargs):
        super(StudentScheduleChoiceForm, self).__init__(*args, **kwargs)
        self.fields['student_schedule'].choices= self.get_student_schedule_choices(self.user.id)
    def get_student_schedule_choices(self, user_id):
        student_schedules = StudentSchedule.objects.filter(student__account__id=user_id).values('id', 'semester__order', 'semester__scholastic__name')
        return [(ss['id'], u'Học kỳ %s Năm học %s' % (ss['semester__order'], ss['semester__scholastic__name'])) for ss in student_schedules]
class OutlineForSubjectChoiceForm(AbstractStudentScheduleGeneratorForm):
    def __init__(self, *args, **kwargs):
        student_schedule_id = self.get_student_schedule_id(kwargs)
        super(OutlineForSubjectChoiceForm, self).__init__(*args, **kwargs)
        outlines = self.get_outlines(student_schedule_id)
        subjects = self.get_subjects_from_outlines(outlines)
        for subject in subjects:
            # TODO initial
            self.fields['outline_%s' % subject.id] = forms.ChoiceField(choices = self.get_outline_choices(subject, outlines),
                                                                    required=True,
                                                                    label=subject.name)
    def get_subjects_from_outlines(self, outlines):
        subjects = []
        for outline in outlines:
            if outline.subject in subjects:
                continue
            subjects.append(outline.subject)
        return subjects
    def get_outline_choices(self, subject, all_outlines):
        outlines = []
        for outline in all_outlines:
            if outline.subject.id != subject.id:
                continue
            outlines.append(outline)
        return [(outline.id, outline) for outline in outlines]
    def get_outlines(self, student_schedule_id):
        subject_ids = SubjectStudentSchedule.objects.filter(student_schedule__id=student_schedule_id).values('subject__id')
        outlines = Outline.objects.filter(subject__id__in=subject_ids).select_related('subject')
        return outlines
    def get_student_schedule_id(self, kwargs):
        return kwargs.pop('student_schedule_id', None)

        