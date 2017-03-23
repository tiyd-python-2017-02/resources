from django.contrib import admin

# Register your models here.
from .models import Task, Status

admin.site.register(Task)
admin.site.register(Status)
