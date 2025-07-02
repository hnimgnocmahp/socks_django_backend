from django.db import models
from .order import Order
from .sock_variant import SockVariant

class OrderItem (models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    sock_variant = models.ForeignKey(SockVariant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    size_name = models.CharField(max_length=20)
    color_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)