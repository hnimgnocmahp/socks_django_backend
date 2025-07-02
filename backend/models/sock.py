from django.db import models
from .category import Category

class Sock(models.Model):
    STATUS_CHOICE = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]
    
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="socks")
    status = models.CharField(max_length=8, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
