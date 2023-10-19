# models.py
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
class Item(models.Model):
    name = models.CharField(max_length=100)  # Ensure item names are unique
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Store total price for the item in the bill
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.customer)
