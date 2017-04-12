from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User)


class Item(models.Model):
    name = models.CharField(max_length=100)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()
