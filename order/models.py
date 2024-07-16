from django.db import models
from product.models import Product
from customer.models import Customer

class Order(models.Model):
    STATUS = {
        "P":"PENDING",
        "C":"CONFIRMED",
        "S":"SHIPPED",
        "D":"DELIVERED"
    }
    customer        = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date      = models.DateTimeField(auto_now_add=True)
    status          = models.CharField(max_length=255, choices=STATUS, default="P")

class OrderItem(models.Model):
    order           = models.ForeignKey(Order, on_delete=models.CASCADE)
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity        = models.PositiveIntegerField()
    price           = models.DecimalField(max_digits=10, decimal_places=2)

class Payment(models.Model):
    METHOD = {
        "T":"TRANSFER",
        "C":"CASH"
    }

    order           = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_date    = models.DateTimeField(auto_now_add=True)
    amount          = models.DecimalField(max_digits=10, decimal_places=2)
    method          = models.CharField(max_length=255, choices=METHOD)