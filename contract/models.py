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
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    services = models.ManyToManyField('ServiceDate')

    def __str__(self):
        return self.name

class ServiceDate(models.Model):
    service_date = models.DateField()
    receipt_image = models.ImageField(upload_to='recps/', blank=True, null=True)

    def __str__(self):
        return str(self.service_date)


class AmountReceived(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='amounts_received')
    received_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)