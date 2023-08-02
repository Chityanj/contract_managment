# contract_management_app/forms.py
from django import forms
from .models import Client, Employee, ServiceDate

class ClientEmployeeForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'contract_start_date', 'contract_expiry_date', 'employees',]
        widgets = {
            'contract_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contract_expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'employees': forms.SelectMultiple(attrs={'class': 'form-control'}),
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