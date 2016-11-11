# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import CreatorModel
from common.models import BaseModel, DescriptionField
from university.models import  Student, Subject, Semester, StudySession, LessionTime
from outline.models import DAY_OF_WEEK_CHOICE
from schedule.models import LEARNING_DAY_TYPE_CHOICES

# Create your models here.
class StudentSchedule(BaseModel, CreatorModel):
    student = models.ForeignKey(Student,
                            blank=False, 
                            null=False,
                            verbose_name=u'Sinh viên')
    semester = models.ForeignKey(Semester,
                                        blank=False,
                                        null=False,
                                        verbose_name=u'Kỳ học')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Lịch học sinh viên'
        verbose_name_plural=verbose_name
    def university_verbose(self):
        return self.student.u_class.course.university
    university_verbose.short_description = u'Đại học'
    @staticmethod
    def autocomplete_search_fields():
        return ("scholastic__name__icontains", "student__email__icontains")
    def __unicode__(self):
        return u'%s %s' %(self.student, self.semester)
class SubjectStudentSchedule(BaseModel, CreatorModel):
    study_session = models.ForeignKey(StudySession,
                                    blank=False, 
                                    null=False,
                                    verbose_name=u'Đợt học')
    student_schedule = models.ForeignKey(StudentSchedule,
                                        blank=False, 
                                        null=False,
                                        verbose_name=u'Lịch học sinh viên')
    subject = models.ForeignKey(Subject,
                                blank=False, 
                                null=False,
                                verbose_name=u'Môn học')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Lịch học sinh viên theo môn'
        verbose_name_plural=verbose_name
    def university_verbose(self):
        return self.student_schedule.university_verbose
    university_verbose.short_description = u'Đại học'
    @staticmethod
    def autocomplete_search_fields():
        return ("student_schedule__scholastic__name__icontains", 
        "student_schedule__student__email__icontains", 
        "subject__code__icontains", 
        "subject__name__icontains")
    def __unicode__(self):
        return u'%s %s' % (self.student_schedule, self.subject)
class LearningDaySubjectSchedule(BaseModel, CreatorModel):
    subject_student_schedule=models.ForeignKey(SubjectStudentSchedule,
                                                blank=False,
                                                null=False,
                                                verbose_name=u'Ngày học')
    day_type=models.SmallIntegerField(blank=False,
                                    choices=LEARNING_DAY_TYPE_CHOICES,
                                    default=0,
                                    verbose_name=u'Giờ')
    day_of_week=models.SmallIntegerField(blank=False, choices=DAY_OF_WEEK_CHOICE,
                                        verbose_name=u'Ngày trong tuần')
    lession_times = models.ManyToManyField(LessionTime,
                                        blank=False,
                                        verbose_name=u'Tiết học')
    place = models.CharField(max_length=100,
                            blank=True,
                            verbose_name=u'Nơi học')
    description = DescriptionField()
    class Meta:
        verbose_name=u'Ngày học của sinh viên theo môn'
        verbose_name_plural=verbose_name
    def university_verbose(self):
        return self.subject_student_schedule.university_verbose
    university_verbose.short_description = u'Đại học'
    @staticmethod
    def autocomplete_search_fields():
        return ("subject_student_schedule__student_schedule__scholastic__name__icontains", 
        "subject_student_schedule__student_schedule__student__email__icontains", 
        "subject_student_schedule__subject__code__icontains", 
        "subject_student_schedule__subject__name__icontains")
    def __unicode__(self):
        return u'%s %s' % (self.day_of_week, self.subject_student_schedule)