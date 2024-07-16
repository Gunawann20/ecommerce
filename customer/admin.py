from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = ['user', 'address', 'joined_on']
    readonly_fields = ['joined_on']
