from django.contrib import admin
from .models import Job, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Job)