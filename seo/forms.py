# -*- coding: utf-8 -*-
from django import forms
from .models import Metatags


class SeoAdminModelForm(forms.ModelForm):
    """
    Класс, добавляющий к форме редактирования СЕО поля
    """
    seo_title = forms.CharField(
        label='SEO title',
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'vTextField'})
    )
    seo_description = forms.CharField(
        label='SEO description',
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'vTextField'})
    )
    seo_keywords = forms.CharField(
        label='SEO keywords',
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'vTextField'})
    )

    def __init__(self, *args, **kwrags):
        """
        Вывод существующих значений метатегов в форму редактирования
        """
        super(SeoAdminModelForm, self).__init__(*args, **kwrags)
        if self.instance.pk:
            try:
                instance_id = self.instance.get_absolute_url()
                metatags = Metatags.objects.get(instance_id=instance_id)

                self.fields['seo_title'].initial = metatags.title
                self.fields['seo_description'].initial = metatags.description
                self.fields['seo_keywords'].initial = metatags.keywords
            except Metatags.DoesNotExist:
                pass
