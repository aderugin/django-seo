# -*- coding: utf-8 -*-
from django.contrib.admin import ModelAdmin
from .forms import SeoAdminModelForm
from .models import Metatags


class SeoAdminMixin(object):
    """
    Миксин, добавляющий метатеги к форме
    """
    form = SeoAdminModelForm

    def save_formset(self, request, form, formset, change):
        """
        Сохранение метатегов для inline елементов
        """
        instances = formset.save()
        for instance in instances:
            for _form in formset:
                if (_form.instance == instance and
                        ('seo_title', 'seo_description', 'seo_keywords') in _form.fields.keys()):
                    self._save_metatags(instance, _form)
                # if f.instance == instance and 'seo_title' in f.fields and 'seo_description' in f.fields\
                #         and 'seo_keywords' in f.fields:
                #     self._save_metatags(instance, f)

    def save_model(self, request, obj, form, change):
        """
        Сохранение метатегов при сохранении изменений в админке
        """
        obj.save()
        self._save_metatags(obj, form)

    def _save_metatags(self, instance, form):
        instance_id = instance.get_absolute_url()
        Metatags.objects.update_or_create(
            instance_id=instance_id,
            defaults={
                'title': form.cleaned_data.get('seo_title'),
                'description': form.cleaned_data.get('seo_description'),
                'keywords': form.cleaned_data.get('seo_keywords')
            }
        )


class SeoAdmin(SeoAdminMixin, ModelAdmin):
    pass
