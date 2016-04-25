# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Metatags(models.Model):
    instance_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    keywords = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __str__(self):
        return self.instance_id

    @classmethod
    def get_metatags(cls, instance_id):
        try:
            return cls.objects.get(instance_id=instance_id)
        except cls.DoesNotExist:
            return {'title': '', 'description': '', 'keywords': ''}
