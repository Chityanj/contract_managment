# contract_management_app/forms.py
from django import forms
from .models import Client, Employee, ServiceDate, AmountReceived

class ClientEmployeeForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'contract_start_date', 'contract_expiry_date', 'employees','amount', ]
        widgets = {
            'contract_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contract_expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'employees': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
class ServiceDateForm(forms.ModelForm):
    class Meta:
        model = ServiceDate
        fields = ['service_date']
        widgets = {
            'service_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class AmountReceivedForm(forms.ModelForm):
    class Meta:
        model = AmountReceived
        fields = ['received_date', 'amount', 'payment_method']
        widgets = {
            'received_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
        }