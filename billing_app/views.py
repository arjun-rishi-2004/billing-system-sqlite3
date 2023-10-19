# views.py
from django.shortcuts import render
from .models import Customer, Item, Bill
from django.shortcuts import render
from .models import Bill

def create_bill(request):
    if request.method == 'POST':
        # Get customer details from the form
        customer_name = request.POST['customer_name']
        mobile_number = request.POST['mobile_number']
        
        # Create a customer object
        customer = Customer.objects.create(name=customer_name, mobile_number=mobile_number)
        
        # Get item details from the form (as arrays)
        item_names = request.POST.getlist('item_name[]')
        prices = request.POST.getlist('price[]')
        quantities = request.POST.getlist('quantity[]')
        
        # Iterate over the items and create Bill objects
        for i in range(len(item_names)):
            item_name = item_names[i]
            price = float(prices[i])
            quantity = int(quantities[i])
            total_price = price * quantity
            
            # Create item object if not exists, or get existing item object
            item, created = Item.objects.get_or_create(name=item_name, price=price)
            
            # Create a bill object for each item
            Bill.objects.create(customer=customer, item=item, quantity=quantity, total_price=total_price)
        
        bills = Bill.objects.filter(customer=customer).select_related('item')

        # Calculate total amount
        total_amount = sum(bill.total_price for bill in bills)

        # Render the bill_display template with the necessary data
        return render(request, 'billing_app/bill_display.html', {
            'customer_name': customer.name,
            'mobile_number': customer.mobile_number,
            'items': bills,
            'total_amount': total_amount
        })
        # Redirect to a success page or generate a bill PDF (using libraries like ReportLab).
        # ...
    else:
        # Render the form template for user input
        return render(request, 'billing_app/billing_app.html')

def excel_view(request):
    # Retrieve bills including associated customer and item information
    bills = Bill.objects.select_related('customer', 'item')

    # Organize bills by customer
    customer_bills = {}
    for bill in bills:
        customer = bill.customer
        if customer not in customer_bills:
            customer_bills[customer] = []

        customer_bills[customer].append(bill)

    # Calculate total price for each customer
    for customer, bills in customer_bills.items():
        total_price = sum(bill.total_price for bill in bills)
        customer.total_price = total_price

    return render(request, 'billing_app/excel_view.html', {'customer_bills': customer_bills})
