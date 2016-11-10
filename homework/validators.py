# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def validate_file_extension(file, valid_extensions):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Không hỗ trợ định dạng file. Vui lòng tải lên các định dạng sau: %s.' % ', '.join(valid_extensions))
def validate_homework_file_extension(file):
	valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls', 'zip', 'rar']
	validate_file_extension(file, valid_extensions)