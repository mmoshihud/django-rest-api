from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Device(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)


class Transaction(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    checkout_condition = models.CharField(max_length=100)
    return_condition = models.CharField(max_length=100, null=True, blank=True)
