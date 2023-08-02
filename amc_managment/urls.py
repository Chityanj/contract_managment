# project_name/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contract.urls')),
    # Add other project-wide URLs here if needed
]
