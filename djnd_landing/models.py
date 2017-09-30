# -*- coding: utf-8 -*-
from django.db import models
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from django.utils.encoding import python_2_unicode_compatible
from tinymce.models import HTMLField

# Create your models here.


class Timestampable(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created_at = AutoCreatedField('creation time')
    updated_at = AutoLastModifiedField('last modification time')

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Exposed(Timestampable):
    category = models.ForeignKey('Category')
    title = models.CharField(max_length=128, default='Izpostavljeno')
    label = HTMLField()
    url = models.URLField(max_length=256, null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.label

@python_2_unicode_compatible
class Category(Timestampable):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
