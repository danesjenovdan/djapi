from django.db import models
from model_utils.fields import AutoCreatedField, AutoLastModifiedField

# Create your models here.


class Timestampable(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created_at = AutoCreatedField(_('creation time'))
    updated_at = AutoLastModifiedField(_('last modification time'))

    class Meta:
        abstract = True


class Exposed(Timestampable):
    category = models.ForeignKey('Category')
    title = models.CharField(max_length=128, default='Izpostavljeno')
    label = models.CharField(max_length=128)
    url = models.URLField(max_length=256)


class Category(Timestampable):
    name = models.CharField(max_length=128)