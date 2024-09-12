from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.IntegerField()
    position = models.CharField(max_length=100)