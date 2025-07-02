from django.db import models
from .sock import Sock
from .color import Color
from .size import Size

class SockVariant(models.Model):
    sock = models.ForeignKey(Sock, on_delete=models.CASCADE, related_name='variants')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)
    stock_quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sock', 'color', 'size')

    def __str__(self):
        return f"{self.sock} - {self.color} - {self.size}"
