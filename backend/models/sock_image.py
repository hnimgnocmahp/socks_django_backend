from django.db import models
from .sock import Sock

class SockImage(models.Model):
    sock = models.ForeignKey(Sock, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='socks_images/')
    alt = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return super().__str__()