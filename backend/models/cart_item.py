from django.db import models
from .customer import Customer
from .sock_variant import SockVariant

class CartItem (models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="cart_item")
    sock_variant = models.ForeignKey(SockVariant, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('customer', 'sock_variant')