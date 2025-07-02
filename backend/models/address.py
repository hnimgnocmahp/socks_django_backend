from django.db import models
from .customer import Customer

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="addresses")
    address_line = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    district = models.CharField(max_length=50, blank=False)
    ward = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return f"{self.address_line} - {self.customer}"
    
    