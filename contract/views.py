# contract_management_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientEmployeeForm, EmployeeForm, ServiceDateForm, AmountReceivedForm
from .models import Client, Employee, ServiceDate , AmountReceived
from datetime import date, timedelta
from django.db.models import Sum

def add_client_employee(request):
    if request.method == 'POST':
        form = ClientEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClientEmployeeForm()
    else:
        form = ClientEmployeeForm()
    return render(request, 'add_client_employee.html', {'form': form})

def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        form = ClientEmployeeForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientEmployeeForm(instance=client)

    return render(request, 'edit_client.html', {'form': form, 'client': client})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()
            
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def private_list_pending_payment(request):
    today = date.today()
    clients = Client.objects.filter(contract_expiry_date__gte=today)
    all_employees = Employee.objects.all()

    for client in clients:
        total_amount_received = client.amounts_received.aggregate(Sum('amount'))['amount__sum']
        if total_amount_received is None:
            total_amount_received = 0
        if total_amount_received >= client.amount:
            clients = clients.exclude(pk=client.pk)

    return render(request, 'client_list.html', {
        'clients': clients,
        'all_employees': all_employees,
    })



def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return redirect('client_list')

def private_list(request):
    today = date.today()
    clients = Client.objects.all()
    employee_name = request.GET.get('employee', None)
    client_name = request.GET.get('client', None)
    all_employees = Employee.objects.all()

    if employee_name:
        clients = clients.filter(employees__name__icontains=employee_name)
    if client_name:  # Apply client name filter
        clients = clients.filter(name__icontains=client_name)

    return render(request, 'client_list.html', {
        'clients': clients,
        'all_employees': all_employees,
    })



def add_amount_received(request, client_id):
    client = Client.objects.get(pk=client_id)

    if request.method == 'POST':
        form = AmountReceivedForm(request.POST)
        if form.is_valid():
            amount_received = form.save(commit=False)
            amount_received.client = client
            amount_received.save()
            return redirect('private_list')
    else:
        form = AmountReceivedForm()

    return render(request, 'add_amount_received.html', {'form': form})


def private_list_soon_to_expire(request):
    today = date.today()
    soon_to_expire_date = today + timedelta(days=45)
    clients = Client.objects.filter(contract_expiry_date__gte=today, contract_expiry_date__lte=soon_to_expire_date)
    all_employees = Employee.objects.all()

    return render(request, 'client_list.html', {
        'clients': clients,
        'all_employees': all_employees,
    })

def public_list(request):
    today = date.today()
    employee_name = request.GET.get('employee', None)
    client_name = request.GET.get('client', None)  # Add client name filter
    clients = Client.objects.filter(contract_expiry_date__gte=today)
    all_employees = Employee.objects.all()

    if employee_name:
        clients = clients.filter(employees__name__icontains=employee_name)

    if client_name:  # Apply client name filter
        clients = clients.filter(name__icontains=client_name)

    return render(request, 'public_list.html', {
        'clients': clients,
        'all_employees': all_employees,
    })


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def add_service_date(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    if request.method == 'POST':
        form = ServiceDateForm(request.POST, request.FILES)
        if form.is_valid():
            service_date = form.save(commit=False)
            service_date.save()
            client.services.add(service_date)
            return redirect('public_list')
    else:
        form = ServiceDateForm()

    return render(request, 'add_service_date.html', {'form': form, 'client': client})

