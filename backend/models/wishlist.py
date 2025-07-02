from django.db import models
from .customer import Customer
from .sock import Sock

class WishList (models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='wishlists')
    sock = models.ForeignKey(Sock, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('customer', 'sock')