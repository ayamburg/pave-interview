from django.db import models


class Employee(models.Model):
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    hire_date = models.DateField()
    employee_type = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    job_level = models.IntegerField()
    location = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    salary = models.DecimalField(decimal_places=2, max_digits=15)
    bonus = models.DecimalField(decimal_places=2, max_digits=15)
    shares = models.DecimalField(decimal_places=2, max_digits=15)
    restaurant = models.CharField(max_length=200)
