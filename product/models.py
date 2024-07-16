from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.TextField()
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.product.name
