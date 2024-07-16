from django.contrib import admin
from .models import Order, OrderItem, Payment

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['customer', 'order_date', 'status']
    readonly_fields = ['order_date']

@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']

@admin.register(Payment)
class AdminPayment(admin.ModelAdmin):
    list_display = ['order', 'payment_date', 'amount', 'method']
    readonly_fields = ['payment_date']
