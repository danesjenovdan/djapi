# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Vote(models.Model):
	type_of = models.CharField(max_length=128)
	time = models.DateTimeField(auto_now_add=True, blank=True)


class MailAddress(models.Model):
	e_mail = models.EmailField()
	type_of = models.CharField(max_length=128)
	name = models.CharField(max_length=128)
	time = models.DateTimeField(auto_now_add=True, blank=True)

	def __unicode__(self):
		return self.name + ' | ' + self.e_mail
