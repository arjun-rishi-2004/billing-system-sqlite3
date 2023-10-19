# billing/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.bill_form, name='bill_form'),  # Define the URL for your billing form
    path('', views.create_bill, name='create_bill'),  # Define the URL for creating a bill
    # Add any additional URLs as needed
    path('excel_view/', views.excel_view, name='excel_view'),
]
