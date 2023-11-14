from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Class Product
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()

# Class Employee
class Employee(models.Model):
    department = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

