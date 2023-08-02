from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=100)
    contract_start_date = models.DateField()
    contract_expiry_date = models.DateField()
    employees = models.ManyToManyField(Employee)
    services = models.ManyToManyField('ServiceDate')

    def __str__(self):
        return self.name

class ServiceDate(models.Model):
    service_date = models.DateField()

    def __str__(self):
        return str(self.service_date)

