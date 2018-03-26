# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *
# Register your models here.

class MailAdmin(admin.ModelAdmin):
    list_filter = ('type_of',)

admin.site.register(Vote)
admin.site.register(MailAddress, MailAdmin)
