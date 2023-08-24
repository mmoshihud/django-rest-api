from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
