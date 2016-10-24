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

from outline.views import OutlineListView, OutlineDetailView, home
from university.views import SubjectListView, SubjectDetailView

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^login/$', views.login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^outline/$', OutlineListView.as_view(), name='outline-list'),
    url(r'^outline/(?P<pk>\d+)/$', OutlineDetailView.as_view(), name='outline-detail'),
    url(r'^subject/$', SubjectListView.as_view(), name='subject-list'),
    url(r'^subject/(?P<pk>\d+)/$', SubjectDetailView.as_view(), name='subject-detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
