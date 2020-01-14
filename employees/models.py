from django.db import models


class Employee(models.Model):
    employeeCode = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    birthDate = models.DateField()
    address = models.TextField()
