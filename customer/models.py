from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    GENDER = {
        "M":"MALE",
        "F":"FEMALE"
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default="Joko")
    last_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, default="M")
    address = models.TextField()
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

