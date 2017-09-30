from django.contrib import admin

# Register your models here.
from .models import *



class ExposedAdmin(admin.ModelAdmin):
    list_display = ('id',
    				'title',
                    'category',)

    list_filter = ('category',)
    search_fields = ['category']

admin.site.register(Category)
admin.site.register(Exposed, ExposedAdmin)