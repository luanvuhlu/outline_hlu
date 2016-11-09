# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path
from django.conf import settings
from django import template

register = template.Library()

@register.filter
def file_extension(file):
    file_info = os.path.splitext(file.name)
    if len(file_info) < 2:
        return None
    return file_info[1][1:]
@register.filter
def file_name(file):
    return os.path.basename(file.name)
@register.filter
def is_image(file):
    ext = ".%s" % file_extension(file)
    print settings.FILEBROWSER_EXTENSIONS['Image']
    return ext in settings.FILEBROWSER_EXTENSIONS['Image']