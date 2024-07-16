from django.contrib import admin
from .models import Category, Product, ProductImage

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

@admin.register(ProductImage)
class AdminProductImage(admin.ModelAdmin):
    list_display = ['product', 'image']
