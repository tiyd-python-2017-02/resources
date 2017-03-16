from django.db import models

# Create your models here.
class Mvp(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    age = models.IntegerField()
    school = models.CharField(max_length=100)
    points = models.DecimalField(max_digits=3, decimal_places=1)
    rebounds = models.DecimalField(max_digits=3, decimal_places=1)
    assists = models.DecimalField(max_digits=3, decimal_places=1)
    steals = models.DecimalField(max_digits=3, decimal_places=1)
    blocks = models.DecimalField(max_digits=3, decimal_places=1)
    shooting_percentage = models.DecimalField(max_digits=4, decimal_places=3)
    three_point_percentage = models.DecimalField(max_digits=4, decimal_places=3)
    free_throw_percentage = models.DecimalField(max_digits=4, decimal_places=3)
