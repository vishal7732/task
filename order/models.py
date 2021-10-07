from django.db import models

# Create your models here.
class Address(models.Model):
    user = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Address_Line_1 = models.CharField(max_length=500)
    Address_Line_2 = models.CharField(max_length=500)
    City = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user

class Orders(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    user = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Address_Line_1 = models.CharField(max_length=500)
    Address_Line_2 = models.CharField(max_length=500)
    City = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)

    def __str__(self):
        return self.product_name