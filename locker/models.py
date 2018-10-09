from django.db import models

# Create your models here.
class Lock(models.Model):
  opened = models.BooleanField(default=False)
  expired = models.BooleanField(default=False)
  code = models.TextField(default='', blank=True)
  activated_at = models.DateTimeField(blank=True, null=True)
  computer = models.TextField(default='', blank=True)