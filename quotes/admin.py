from django.contrib import admin

# Register your models here.
##### file: quotes/admin.py #####

from .models import Quote
admin.site.register(Quote)