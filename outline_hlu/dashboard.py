# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            u'Ứng dụng',
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',),
        ))
        # Column 2
        # Thêm link cho các chức năng mở rộng
        self.children.append(modules.LinkList(
            u'Chức năng mở rộng',
            column=2,
            children=[
                {
                    'title': u'Tạo lịch học',
                    'url': '/student-schedule-genrator/1/',
                    'external': False,
                },
            ]
        ))
        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('Administration'),
            column=2,
            collapsible=True,
            models=('django.contrib.*',),
        ))
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            u'Quản lý đa phương tiện',
            column=2,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            u'Hỗ trợ',
            column=2,
            children=[
                {
                    'title': u'Tài liệu Django',
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': u'Tài liệu Grappelli',
                    'url': 'http://django-grappelli.readthedocs.io/en/latest/',
                    'external': True,
                },
            ]
        ))
        # Column 3
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=20,
            collapsible=True,
            column=3,
        ))


