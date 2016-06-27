from django.db import models

# Create your models here.

class Vote(models.Model):
	type_of = models.CharField(max_length=128)
	time = models.DateTimeField(auto_now_add=True, blank=True)