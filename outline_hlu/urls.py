"""outline_hlu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site

from account.views import RegistrationView
from outline.views import OutlineListView, OutlineDetailView, home
from homework.views import HomeWorkDetailView, HomeWorkListView, HomeWorkQuestionView
from university.views import SubjectListView, SubjectDetailView, SpecializedStudyListView, SpecializedStudyDetailView
from student_schedule.views import StudentScheduleGeneratorView, StudentScheduleGeneratorOutlineForSubjectView, StudentScheduleDetailView
urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^login/$', views.login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^signup/$', RegistrationView.as_view(), name='signup'),
    url(r'^outline/$', OutlineListView.as_view(), name='outline_list'),
    url(r'^outline/(?P<pk>\d+)/$', OutlineDetailView.as_view(), name='outline_detail'),
    url(r'^subject/$', SubjectListView.as_view(), name='subject_list'),
    url(r'^subject/(?P<pk>\d+)/$', SubjectDetailView.as_view(), name='subject_detail'),
    url(r'^specialized-study/$', SpecializedStudyListView.as_view(), name='specialized_study_list'),
    url(r'^specialized-study/(?P<pk>\d+)/$', SpecializedStudyDetailView.as_view(), name='specialized_study_detail'),
    url(r'^homework/$', HomeWorkListView.as_view(), name='home_work_list'),
    url(r'^homework/(?P<pk>\d+)/$', HomeWorkDetailView.as_view(), name='home_work_detail'),
    url(r'^homework/(?P<pk>\d+)/question/$', HomeWorkQuestionView.as_view(), name='homework_question'),
    # url(r'^student-schedule-genrator/0/$', StudentScheduleCreateView.as_view(), name='student_schedule_create'),
    url(r'^student-schedule-genrator/1/$', StudentScheduleGeneratorView.as_view(), name='student_schedule_generator_choice_1'),
    url(r'^student-schedule-detail/(?P<pk>\d+)/$', StudentScheduleDetailView.as_view(), name='student_schedule_detail'),
    url(r'^student-schedule-genrator/2/$', StudentScheduleGeneratorOutlineForSubjectView.as_view(), name='student_schedule_generator_choice_2'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
