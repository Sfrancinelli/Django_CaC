from django.db import models

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_lenght=30)
    address = models.CharField(max_lenght=80)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_lenght=10)

class Products(models.Model):
    name = models.CharField(max_lenght=30)
    section = models.CharField(max_lenght=30)
    price = models.IntegerField()

class Orders(models.Model):
    order_id = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()
