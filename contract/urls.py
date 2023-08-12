# contract_management_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_client_employee/', views.add_client_employee, name='add_client_employee'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('private/', views.private_list, name='client_list'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('add_service_date/<int:client_id>/', views.add_service_date, name='add_service_date'),
    path('', views.public_list, name='public_list'),
    path('private_list_soon_to_expire/', views.private_list_soon_to_expire, name='private_list_soon_to_expire'),
    path('delete-client/<int:client_id>/', views.delete_client, name='delete_client'),
    path('private_list_pending_payment/', views.private_list_pending_payment, name='private_list_pending_payment'),
    path('add_amount_received/<int:client_id>/', views.add_amount_received, name='add_amount_received'),
]
