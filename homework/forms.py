# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django import forms
from django.db import transaction, IntegrityError
from multiupload.fields import MultiFileField
from models import HomeWorkQuestionAttachment, HomeWorkQuestion, HomeWork
from validators import validate_homework_file_extension
from common.managers import handle_uploaded_file

logger = logging.getLogger(__name__)

class HomeWorkQuestionForm(forms.ModelForm):
    class Meta:
        model = HomeWorkQuestion
        fields = ['no', 'content']
    content = forms.CharField(label=u'Nội dung',
                        max_length=500,
                        help_text=u'Có thể đính kèm file thay vì nhập mục này',
                        required=False,
                        widget=forms.Textarea)
    attachments = MultiFileField(label=u'Đính kèm',
                        min_num=1,
                        max_num=5,
                        help_text=u'Chọn ít nhất một file và không quá 5 file. <br />Nếu quá 5 file, vui lòng nén lại và đính kèm ít file hơn',
                        max_file_size=1024*1024*5,
                        required=False)
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.home_work_id = kwargs.pop('home_work_id', None)
        super(HomeWorkQuestionForm, self).__init__(*args, **kwargs)
    def clean(self):
        if not self.user:
            raise forms.ValidationError(u'Không tìm thấy thông tin đăng nhập')
        if not self.home_work_id:
            raise forms.ValidationError(u'Không tìm thấy thông tin bài tập')
        cleaned_data = super(HomeWorkQuestionForm, self).clean()
        if not cleaned_data.get('content') and not cleaned_data.get('attachments'):
            raise forms.ValidationError(u'Phải nhập nội dung hoặc đính kèm file')
        for file in cleaned_data['attachments']:
            validate_homework_file_extension(file)
    def save(self, commit=True):
        instance = super(HomeWorkQuestionForm, self).save(commit=False)
        instance.creator = self.user
        if not instance.no:
            instance.no = u'Tất cả'
        instance.home_work = HomeWork.objects.get(id=self.home_work_id)
        if not commit:
            return instance
        try:
            with transaction.atomic():
                instance.save()
                for file in self.cleaned_data['attachments']:
                    attachment = HomeWorkQuestionAttachment(document=handle_uploaded_file(file, 'questions'), 
                                                            question=instance)
                    attachment.creator = self.user
                    attachment.save()
        except (IntegrityError, AttributeError, IOError) as e:
            logger.error(u'Đã có lỗi xảy ra, vui lòng thử lại: %s' % e.message)
            ## TODO Debug
            raise e
            # raise forms.ValidationError(u'Đã có lỗi xảy ra, vui lòng thử lại: %(error)s',
            #                             params={'error': e.message})
        return instance 
    