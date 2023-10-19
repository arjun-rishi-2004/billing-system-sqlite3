# admin.py
from django.contrib import admin
from .models import Customer, Item, Bill

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Bill)
