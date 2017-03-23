from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=20)
    priority = models.IntegerField()

class Task(models.Model):
    description = models.CharField(max_length=500)
    status = models.ForeignKey(Status)
