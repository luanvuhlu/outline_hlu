# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path
import sys
from datetime import date 
from django.conf import settings

def handle_uploaded_file(file, folder, insert_time=True):
    if insert_time:
        relative_path = os.path.join(folder, date.today().strftime('%Y/%m/%d/'))
    else:
        relative_path = folder
    # filename = os.path.basename(file.name)
    path_with_name = os.path.join(relative_path, file.name)
    full_path, path_with_name = avoid_dupplicate_file(settings.MEDIA_ROOT, path_with_name)
    # full_path = os.path.join(settings.MEDIA_ROOT, path_with_name)
    with open(full_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return path_with_name
def mkdir_p(path):
    if os.path.isdir(path):
        return
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            pass
        else: raise
def avoid_dupplicate_file(root_folder, path_with_name):
    i = 0
    full_path = os.path.join(root_folder, path_with_name)
    while True:
        if os.path.isfile(full_path):
            i+= 1
        break
        if i:
            fname, ext = os.path.splitext(full_path)
            full_path = fname + str(i) + '.' + ext
            path_with_name = fname + str(i) + '.' + ext
    mkdir_p(os.path.dirname(full_path))
    return full_path, path_with_name